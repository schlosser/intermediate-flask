from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

# Import and register the Blueprints
from app.routes.blog import blog
from app.routes.home import home
app.register_blueprint(blog)
app.register_blueprint(home)
