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

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', 
        title = 'YoSe ~ Acerca de mi'
        )

@app.route('/minesweeper')
def minesweeper():
    return render_template('minesweeper.html',
        title = 'Minesweeper',
        rows = range(1, 9),
        cols = range(1, 9),
        )


@app.route('/primeFactors')
def primeFactors():
    from primes import factors

    def get_result(n):
        try:
            n = int(n)
        except ValueError:
            return {
                "number": n,
                "error" : 'not a number',
                }
        if n > 1e6:
            return {
                "number": n,
                "error" : "too big number (>1e6)",
                }
        else:
            return {
                "number": n,
                "decomposition" : factors(n)
                }

    numbers = request.args.getlist('number')
    if len(numbers) > 1:
        result = [get_result(n) for n in numbers]
    else:
        result = get_result(numbers[0])
    r = Response(json.dumps(result, indent=4), mimetype="application/json")
    return r

