from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes.notebooks import notebooks_bp
from routes.metadata import metadata_bp
from routes.workflow import workflow_bp
from routes.clusters import clusters_bp
from utils.config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configurations from utils/config.py
app.config.from_object(Config)

# Enable CORS for cross-origin requests
CORS(app)

# Initialize the database
db = SQLAlchemy(app)

# Register blueprints for modular routing
app.register_blueprint(notebooks_bp, url_prefix="/api/notebooks")
app.register_blueprint(metadata_bp, url_prefix="/api/metadata")
app.register_blueprint(workflow_bp, url_prefix="/api/workflow")
app.register_blueprint(clusters_bp, url_prefix="/api/clusters")

# Default route to check if the server is running
@app.route('/')
def home():
    return jsonify({"message": "Welcome to DataHarbor Backend API"})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

