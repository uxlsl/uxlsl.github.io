# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.script import Manager
from flask import request


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1> hello, %s!</h1>' % name


@app.route('/request')
def headers():
    return '%s' % request.headers


if __name__ == '__main__':
    manager.run()
