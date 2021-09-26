from flask import render_template

from . import main

@main.route('/')
def home():
    """
    function to return home template
    :return: home.html
    """
    return render_template('home.html')