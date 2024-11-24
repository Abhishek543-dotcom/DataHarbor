from flask import Flask
from routes import notebooks, metadata, workflow, clusters
from utils.db import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@db:5432/dataharbor'

init_db(app)

# Register Blueprints
app.register_blueprint(notebooks.bp)
app.register_blueprint(metadata.bp)
app.register_blueprint(workflow.bp)
app.register_blueprint(clusters.bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
