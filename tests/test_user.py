import unittest

from app.models import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(username='zoo', email="zoo@test.com", bio='default bio', password='pswd1234')

    def test_password_setter(self):
        self.assertTrue(self.new_user.secure_password is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('pswd1234'))

    def test_user(self):
        self.assertEqual(self.new_user.username, 'zoo')
        self.assertEqual(self.new_user.email, 'zoo@test.com')
        self.assertEqual(self.new_user.bio, 'default bio')
