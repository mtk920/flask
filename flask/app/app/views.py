from flask import render_template
from . import main

@main.route('/', method=['GET', 'POST'])
def index():
    print('!!!')
    return render_template('index.html')
