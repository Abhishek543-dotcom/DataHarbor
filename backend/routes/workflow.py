from flask import Blueprint, jsonify, request

# Define the Blueprint for workflows
workflow_bp = Blueprint('workflow', __name__)

# Dummy workflows data
workflows = [
    {"id": 1, "name": "ETL Pipeline", "status": "Completed"},
    {"id": 2, "name": "Data Cleaning", "status": "In Progress"}
]

# Route to fetch all workflows
@workflow_bp.route('/workflows', methods=['GET'])
def get_all_workflows():
    return jsonify({"workflows": workflows}), 200

# Route to fetch a specific workflow by ID
@workflow_bp.route('/workflows/<int:workflow_id>', methods=['GET'])
def get_workflow_by_id(workflow_id):
    workflow = next((wf for wf in workflows if wf["id"] == workflow_id), None)
    if workflow:
        return jsonify(workflow), 200
    return jsonify({"error": "Workflow not found"}), 404
