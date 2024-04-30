#!/usr/bin/python3
"""index.py"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """Returns status OK"""
    return jsonify({"status": "OK"})


@app_views.route('/status', methods=['GET'])
def stasts():
    """Retrieves the number of each objects by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    resp = jsonify(stats)
    resp.status_code = 200

    return resp
