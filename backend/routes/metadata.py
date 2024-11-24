from flask import Blueprint, jsonify

# Define the Blueprint for metadata
metadata_bp = Blueprint('metadata', __name__)

# Dummy metadata information
metadata_info = {
    "app_name": "DataHarbor",
    "version": "1.0.0",
    "description": "A data management platform for notebooks, workflows, and clusters."
}

# Route to fetch metadata
@metadata_bp.route('/metadata', methods=['GET'])
def get_metadata():
    return jsonify(metadata_info), 200
