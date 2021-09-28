import unittest
from app.models import UserComment, Blog, User
from app.commands import db


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_zoo = User(username='zoo', password='pswd1234', email='zoo@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_zoo.id)
        self.new_comment = UserComment(id=1, comment='This is a test comment', user_id=self.user_zoo.id,
                                   blog_id=self.new_blog.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        UserComment.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'This is a test comment')
        self.assertEquals(self.new_comment.user_id, self.user_zoo.id)
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(db.session.query(UserComment)) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        res_comment = UserComment.get_comment(1)
        self.assertTrue(res_comment is not None)
