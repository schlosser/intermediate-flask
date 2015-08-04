from flask import Blueprint, render_template, redirect, url_for, request
from app.models.blog import BlogPost, BlogPostForm

# Create the blog Blueprint.  Note that all routes on the blog blueprint have
# '/blog' prepended to them.
blog = Blueprint('blog', __name__, url_prefix='/blog')

@blog.route('/')  # Accessible at /blog/
def blog_page():
    """The blog page."""
    # objects() is a Flask-Mongoengine method that returns all of the BlogPost objects.
    posts = BlogPost.objects()
    return render_template('blog.html', posts=posts)

@blog.route('/new', methods=['GET', 'POST'])
def new():
    """Create a new post"""
    form = BlogPostForm(request.form)

    if request.method =='POST' and form.validate():
        # form.save() is a Flask-Mongoengine method that creates an entry in 
        # mongoDB. The form object is populated by the values entered into the form
        # on page's view. For secure applications with other databases
        # , you might add methods here to sanitize the submitted data and reject 
        # dangerous inputs. See: http://bobby-tables.com/
        form.save()
        return redirect(url_for('blog.blog_page'))

    return render_template('new.html', form =form)

@blog.route('/view/<id>')
# grab post ObjectID parameter to have a static URL for people to bookmark.
# #If you skip the <id> part of the route, each blog post will appear at 
# localhost:5000/view/, and only accessible by clicking through the blog page.
def view(id):
    """View contents of a blog post"""
    # Retrive post comment using mongoEngine
    post = BlogPost.objects.get_or_404(id=id)
    return render_template('post.html', post=post)
