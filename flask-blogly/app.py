"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """Redirect to users page."""
    return redirect('/users')

@app.route('/users')
def users():
    """Show users page with links to user details."""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET'])
def new_form():
    """Show new user form"""

    return render_template('new.html')

@app.route('/users/new', methods=['POST'])
def add_new():
    """Make new user from form, add to database, and redirect to users page"""
    f_name = request.form['first-name']
    l_name = request.form['last-name']
    img_url = request.form['image-url']

    new_user = User(first_name=f_name, last_name=l_name, image_url=img_url or None)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def details(user_id):
    """Show specific user details with edit and delete page"""

    user = User.query.get_or_404(user_id)

    return render_template('details.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def edit(user_id):
    """Show edit users forms"""

    user = User.query.get_or_404(user_id)

    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def send_edit(user_id):
    """Edit / Update user info from form"""

    edit_user = User.query.get_or_404(user_id)

    edit_user.first_name = request.form['first-name']
    edit_user.last_name = request.form['last-name']
    edit_user.image_url = request.form['image-url'] or None

    db.session.add(edit_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete(user_id):
    """Remove user from users database"""

    db.session.delete(User.query.get_or_404(user_id))
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new')
def new_post_form(user_id):
    """Show form to add a post for that user"""

    user = User.query.get_or_404(user_id)

    return render_template('new_post.html', user=user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    """Handle add form; add post and redirect to the user detail page"""

    title = request.form['title']
    content = request.form['content']
    user = User.query.get_or_404(user_id)

    new_post = Post(title=title, content=content, user=user)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')

# Post routes

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """Show a post. Show buttons to edit and delete the post"""

    post = Post.query.get_or_404(post_id)

    return render_template('post.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    """Show form to edit a post, and to cancel (back to user page)"""

    post = Post.query.get_or_404(post_id)

    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def handle_edit(post_id):
    """Handle editing post. Redirect back to the post view."""

    edit_post = Post.query.get_or_404(post_id)

    edit_post.title = request.form['title']
    edit_post.content = request.form['content']
    
    db.session.add(edit_post)
    db.session.commit()

    return redirect(f'/posts/{post_id}')



@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """Delete the post"""

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f'/users/{post.user_id}')