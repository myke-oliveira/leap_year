#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:09:09 2019

@author: myke
"""

from flask import Flask, render_template, url_for, request
from leap_year import is_leap_year
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index(result=None):
    print(request.method)
    if request.method == 'POST':
        year = int(request.form['year'])
        result = f'{year}: {"Leap Year" if is_leap_year(year) else "Not a Leap Year"}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
