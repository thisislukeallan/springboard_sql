from unittest import TestCase

from app import app
from models import db, User, Post
from flask import url_for, request
from datetime import datetime

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for Users"""

    def setUp(self):
        """Add sample user."""

        Post.query.delete()
        User.query.delete()

        user = User(first_name="First", last_name="Last", image_url='https://picsum.photos/200')

        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
        self.user = user

    def tearDown(self):
        """Clean up unused transactions."""

        # db.session.rollback()

    def test_users_redirect(self):
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            assert response.request.path == url_for('users')

    def test_list_users(self):
        with app.test_client() as client:
            response = client.get('/users')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<li><a href=', html)

    def test_show_user(self):
        with app.test_client() as client:
            response = client.get(f"/users/{self.user_id}")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>First Last</h1>', html)
            self.assertIn(self.user.last_name, html)

    def test_add_user(self):
        with app.test_client() as client:
            u = {"first-name": "First2", "last-name": "Last2", "image-url": "https://picsum.photos/200"}
            response = client.post("/users/new", data=u, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("First2 Last2", html)

    # Posts tests

    def test_add_post(self):
        with app.test_client() as client:
            p = {"title": "Test Title", "content": "Test Content. Foo bar. Testing: one, two, three", "user_id": f"{self.user_id}"}
            response = client.post(f"/users/{self.user_id}/posts/new", data=p, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("Test Title", html)

    def test_list_posts(self):
        with app.test_client() as client:

            post = Post.query.first()
            self.post_id = post.id

            response = client.get(f'/posts/{self.post_id}')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Title', html)
            self.assertIn(self.post.title)

    def test_edit_form(self):
        with app.test_client() as client:
            response = client.get(f'/posts/{self.post_id}/edit')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Edit', html)
