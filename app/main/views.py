from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from . import main
from app.models import User, Blog, UserComment, Subscriber
from .forms import UpdateProfile, CreateBlog
from app.quotes_request import get_quotes
from ..commands import db
from ..send_email import mail_message


@main.route('/')
def home():
    """
    function to return home template
    :return: home.html
    """
    quotes = get_quotes()
    page = request.args.get('page', 1, type=int)
    blogs = db.session.query(Blog).order_by(db.desc(Blog.date_posted)).paginate(page=page, per_page=5)
    return render_template('home.html', quotes=quotes, blogs=blogs)


@main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.profile_picture.data:
            picture_file = save_picture(form.profile_picture.data)
            current_user.profile_pic_path = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('Successfully updated your profile')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    profile_pic_path = url_for('static', filename='photos/' + current_user.profile_pic_path)
    return render_template('user-profile/user-profile.html', profile_pic_path=profile_pic_path, form=form)


@main.route('/user/<name>/profile_update', methods=['POST', 'GET'])
@login_required
def profile_update(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.profile', name=name))
    return render_template('user-profile/update-user-profile.html', form=form)


@main.route('/new_post', methods=['POST', 'GET'])
@login_required
def new_blog():
    subscribers = db.session.query(Subscriber).all()
    form = CreateBlog()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user._get_current_object().id
        blog = Blog(title=title, content=content, user_id=user_id)
        blog.save()
        for subscriber in subscribers:
            mail_message("New Blog Post", "email/new_blog", subscriber.email, blog=blog)
        flash('You Posted a new Blog')
        return redirect(url_for('main.index'))

    return render_template('new-blog.html', form=form)


@main.route('/blog/<id>')
def blog(id):
    comments = db.session.query(UserComment).filter_by(blog_id=id).all()
    blog = db.session.query(Blog).get(id)
    return render_template('blog.html', blog=blog, comments=comments)


@main.route('/blog/<blog_id>/update', methods=['GET', 'POST'])
@login_required
def blog_update(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    form = CreateBlog()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.content = form.content.data
        db.session.commit()
        flash("You have updated your Blog!")
        return redirect(url_for('main.blog', id=blog.id))
    if request.method == 'GET':
        form.title.data = blog.title
        form.content.data = blog.content
    return render_template('new-blog.html', form=form)


@main.route('/comment/<blog_id>', methods=['Post', 'GET'])
@login_required
def comment(blog_id):
    blog = db.session.query(Blog).get(blog_id)
    comment = request.form.get('newcomment')
    new_comment = UserComment(comment=comment, user_id=current_user._get_current_object().id, blog_id=blog_id)
    new_comment.save()
    return redirect(url_for('main.blog', id=blog.id))


@main.route('/subscribe', methods=['POST', 'GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email=email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to D-Blog", "email/welcome_subscriber", new_subscriber.email,
                 new_subscriber=new_subscriber)
    flash('Subscription successful')
    return redirect(url_for('main.home'))


@main.route('/blog/<blog_id>/delete', methods=['POST'])
@login_required
def delete_post(blog_id):
    blog = db.session.query(Blog).get(blog_id)
    if blog.user != current_user:
        abort(403)
    blog.delete()
    flash("Blog deleted successfully")
    return redirect(url_for('main.home'))


@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first()
    page = request.args.get('page', 1, type=int)
    blogs = Blog.query.filter_by(user=user).order_by(Blog.posted.desc()).paginate(page=page, per_page=4)
    return render_template('user-posts.html', blogs=blogs, user=user)
