import unittest
from app.models import Blog, User
from app.commands import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_zoo = User(username='zoo', password='pswd1234', email='test@test.com')
        self.new_blog = Blog(id=1, title='Test', content='This is a test blog', user_id=self.user_zoo.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_zoo.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(db.session.query(Blog)) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        res_blog = Blog.get_blog(1)
        self.assertTrue(res_blog is not None)
