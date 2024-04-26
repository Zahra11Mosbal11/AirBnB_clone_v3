#!/usr/bin/python3
"""index.py"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns status OK"""
    return jsonify({"status": "OK"})
