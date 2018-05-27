#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Flask App
@author: bilal
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello my XX friend!"


if __name__ == "__main__":
    app.run(host = 'localhost',port = 5000, debug = True)
    