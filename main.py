#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello Yose'

@app.route('/ping')
def ping():
    return '{ "alive": true}'
