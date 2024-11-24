from flask import Blueprint, jsonify, request

# Define the Blueprint for notebooks
notebooks_bp = Blueprint('notebooks', __name__)

# Dummy data for notebooks
notebooks = [
    {"id": 1, "title": "Introduction to Data Science", "author": "John Doe"},
    {"id": 2, "title": "Machine Learning Basics", "author": "Jane Smith"},
    {"id": 3, "title": "Deep Learning with Python", "author": "Alice Johnson"}
]

# Route to fetch all notebooks
@notebooks_bp.route('/notebooks', methods=['GET'])
def get_all_notebooks():
    return jsonify({"notebooks": notebooks}), 200

# Route to fetch a specific notebook by ID
@notebooks_bp.route('/notebooks/<int:notebook_id>', methods=['GET'])
def get_notebook_by_id(notebook_id):
    notebook = next((nb for nb in notebooks if nb["id"] == notebook_id), None)
    if notebook:
        return jsonify(notebook), 200
    return jsonify({"error": "Notebook not found"}), 404

# Route to create a new notebook
@notebooks_bp.route('/notebooks', methods=['POST'])
def create_notebook():
    data = request.get_json()
    if not data or not all(key in data for key in ["title", "author"]):
        return jsonify({"error": "Invalid data"}), 400
    new_id = max(nb["id"] for nb in notebooks) + 1 if notebooks else 1
    new_notebook = {"id": new_id, "title": data["title"], "author": data["author"]}
    notebooks.append(new_notebook)
    return jsonify(new_notebook), 201

# Route to update an existing notebook by ID
@notebooks_bp.route('/notebooks/<int:notebook_id>', methods=['PUT'])
def update_notebook(notebook_id):
    data = request.get_json()
    notebook = next((nb for nb in notebooks if nb["id"] == notebook_id), None)
    if not notebook:
        return jsonify({"error": "Notebook not found"}), 404
