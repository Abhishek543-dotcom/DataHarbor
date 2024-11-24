from flask import Blueprint

# Define blueprints for modular routes
notebooks_blueprint = Blueprint('notebooks', __name__)
metadata_blueprint = Blueprint('metadata', __name__)
workflow_blueprint = Blueprint('workflow', __name__)
clusters_blueprint = Blueprint('clusters', __name__)

# Import routes
from . import notebooks, metadata, workflow, clusters
