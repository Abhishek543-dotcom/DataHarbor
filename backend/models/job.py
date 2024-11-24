from . import db

class Job(db.Model):
    __tablename__ = 'jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.id'), nullable=False)
    cluster_id = db.Column(db.Integer, db.ForeignKey('clusters.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), default="Pending")  # Status can be Pending, Running, Completed, Failed
    
    # Relationships
    notebook = db.relationship('Notebook', backref=db.backref('jobs', lazy=True))
    cluster = db.relationship('Cluster', backref=db.backref('jobs', lazy=True))

    def __repr__(self):
        return f'<Job {self.name} - Status: {self.status}>'
