from flask import Flask
from flask_cors import CORS
from routes.notebooks import notebooks_bp
from routes.metadata import metadata_bp
from routes.workflow import workflow_bp
from routes.clusters import clusters_bp

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS to allow cross-origin requests
CORS(app)

# Register blueprints for each route module
app.register_blueprint(notebooks_bp, url_prefix='/api')
app.register_blueprint(metadata_bp, url_prefix='/api')
app.register_blueprint(workflow_bp, url_prefix='/api')
app.register_blueprint(clusters_bp, url_prefix='/api')

# Define a default route for health check
@app.route('/')
def health_check():
    return {"status": "OK", "message": "Backend is running!"}, 200

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
