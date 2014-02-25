#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask import Response
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ping')
def ping():
    r = Response('{ "alive": true}', mimetype="application/json")
    return r
