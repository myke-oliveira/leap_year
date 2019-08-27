#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:09:09 2019

@author: myke
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
