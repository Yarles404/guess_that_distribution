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

DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
POSTGRES_PASSWORD=os.environ['POSTGRES_PASSWORD']
POSTGRES_USER=os.environ['POSTGRES_USER']
POSTGRES_DB=os.environ['POSTGRES_DB']

connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

# PostgreSQL db
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(plays)

if __name__ == '__main__':
    app.run(debug=True)