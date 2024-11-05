#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
"""
function returns render template
"""


def index():
    return render_template('0-index.html')


"""
run the app
"""
if __name__ == '__main__':
    app.run(debug=True)
