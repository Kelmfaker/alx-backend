#!/usr/bin/env python3
"""
This module sets up a Flask app with Babel for internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.

    Returns:
        str: The best match for supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Render the index.html template.

    Returns:
        str: The rendered template.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
