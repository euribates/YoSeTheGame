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
    numbers = request.args.getlist('number')
    result = []
    for number in numbers:
        try:
            number = int(number)
            if number > 1e6:
                result.append({
                    "number": number,
                    "error" : "too big number (>1e6)",
                    })
            else:
                result.append({
                    "number": number,
                    "decomposition" : factors(number)
                    })

        except ValueError as err:
            result.append({
                "number": number,
                "error" : 'not a number',
                }) 

    r = Response(json.dumps(result, indent=4), mimetype="application/json")
    return r

