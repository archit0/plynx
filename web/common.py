#!/usr/bin/env python
from flask import Flask, render_template, request, send_file, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def urls_for():
    pass
    url_for('static', filename='style.css')
    url_for('static', filename='favicon.png')