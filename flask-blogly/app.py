"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

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

