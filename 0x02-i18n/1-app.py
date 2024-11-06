#!/usr/bin/env python3
"""
Basic Babe setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configurate the app language
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Render the index.html template.
    Returns:
    str: The rendered template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
