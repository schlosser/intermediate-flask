from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = { 'db': 'blask' }

db = MongoEngine(app)

# Import and register the Blueprints
from app.routes.blog import blog
from app.routes.home import home
app.register_blueprint(blog)
app.register_blueprint(home)
