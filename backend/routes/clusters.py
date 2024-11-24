from flask import Blueprint, jsonify, request

# Define the Blueprint for clusters
clusters_bp = Blueprint('clusters', __name__)

# Dummy clusters data
clusters = [
    {"id": 1, "name": "Cluster A", "status": "Active"},
    {"id": 2, "name": "Cluster B", "status": "Inactive"}
]

# Route to fetch all clusters
@clusters_bp.route('/clusters', methods=['GET'])
def get_all_clusters():
    return jsonify({"clusters": clusters}), 200

# Route to fetch a specific cluster by ID
@clusters_bp.route('/clusters/<int:cluster_id>', methods=['GET'])
def get_cluster_by_id(cluster_id):
    cluster = next((cl for cl in clusters if cl["id"] == cluster_id), None)
    if cluster:
        return jsonify(cluster), 200
    return jsonify({"error": "Cluster not found"}), 404
