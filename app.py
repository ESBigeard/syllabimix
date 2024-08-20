#!/usr/bin/python
# -*- coding:utf-8 -*-


import flask
import json


app=flask.Flask(__name__)

@app.route("/")
def index():
	return flask.render_template("index.html")

