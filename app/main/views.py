from flask import render_template, session, redirect, url_for, current_app
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')