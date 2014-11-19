from flask import Blueprint, render_template
from app.models.blog import BlogPost

# Create the blog Blueprint.  Note that all routes on the blog blueprint have
# '/blog' prepended to them.
blog = Blueprint('blog', __name__, url_prefix='/blog')


@blog.route('/')  # Accessible at /blog/
def blog_page():
    """The blog page."""
    posts = BlogPost.objects()
    return render_template('blog.html', posts=posts)
