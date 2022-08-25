from flask import Flask, session
from blueprints.plays import plays
import redis
from flask_sqlalchemy import SQLAlchemy
import os

# Create the application
app = Flask(__name__)

# Config
app.secret_key = os.environ['SECRET_KEY']
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url(os.environ['REDIS_URL'])

# PostgreSQL db
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(plays)

if __name__ == '__main__':
    app.run(debug=True)