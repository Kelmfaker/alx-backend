#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

"""
Function index
"""
@app.route('/')
def index():
    """
    return render template
    """
    return render_template('0-index.html')


# debugging
if __name__ == '__main__':
    """
    run debug
    """
    app.run(debug=True)
