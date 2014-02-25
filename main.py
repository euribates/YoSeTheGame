#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello Yose'

@app.route('/ping')
def ping():
    r = Response('{ "alive": true}', mimetype="application/json")
    return r
