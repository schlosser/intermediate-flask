from flask import Blueprint, render_template

home = Blueprint('home', __name__)

@home.route('/')
def home_page():
    """The home page."""
    return render_template('home.html')
