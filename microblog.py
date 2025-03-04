from flask import Flask
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


app = Flask(__name__)

if __name__ == '__main__':
    app.run()
