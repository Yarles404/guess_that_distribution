from flask import Flask
from blueprints.play import play

# Create the application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(play)


if __name__ == '__main__':
    app.run(debug=True)