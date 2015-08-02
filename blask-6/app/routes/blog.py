from flask import Blueprint, render_template, redirect, url_for, request
#last 3 imports are for the new form
from app.models.blog import BlogPost, BlogPostForm

# Create the blog Blueprint.  Note that all routes on the blog blueprint have
# '/blog' prepended to them.
blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')  # Accessible at /blog/
def blog_page():
    """The blog page."""
    #objects() method comes from the Flask mongoengine
    posts = BlogPost.objects()
    return render_template('blog.html', posts=posts)

@blog.route('/new', methods=['GET', 'POST'])
def new():
    """Create a new post"""
    form = BlogPostForm(request.form)

    if request.method =='POST' and form.validate():
        form.save()
        return redirect(url_for('blog.blog_page'))

    return render_template('new.html', form =form)

@blog.route('/view/<id>')
# grab postObjectID parameter to have a static URL for people to bookmark.
def view(id):
    """View contents of a blog post"""
    # Retrive post comment using mongoEngine
    post = BlogPost.objects.get_or_404(id=id)
    return render_template('post.html', post=post)
