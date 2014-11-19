from mongoengine import connect
from app.models.blog import BlogPost

connect('blask')
BlogPost.drop_collection()
post1 = BlogPost(author='Cecelia Coder',
                 title='My First Blog Post',
                 body='Who knew this could be so easy?')
post2 = BlogPost(author='Cecelia Coder',
                 title='Flask is Fun',
                 body='Everything is better with Mongoengine!')
post1.save()
post2.save()
