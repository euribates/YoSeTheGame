#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import os

from flask import Flask
from flask import Response
from flask import render_template
from flask import request

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ping')
def ping():
    r = Response('{ "alive": true}', mimetype="application/json")
    return r

@app.route('/primeFactors')
def primeFactors():
    from primes import factors
    number = int(request.args.get('number', 16))
    r = Response(
        json.dumps({
            "number": number,
            "decomposition" : factors(number)
            }), 
        mimetype="application/json"
        )
    return r
