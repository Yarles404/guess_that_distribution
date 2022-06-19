from flask import Flask
from blueprints import *

# Create the application
app = Flask(__name__)

# Register blueprints


if __name__ == '__main__':
    app.run(debug=True)