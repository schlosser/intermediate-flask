#What it does is import the Flask instance called app from app/__init__.py, and call app.run() on it once the script is executed.
from app import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)