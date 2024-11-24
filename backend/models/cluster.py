from . import db

class Cluster(db.Model):
    __tablename__ = 'clusters'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ram = db.Column(db.Integer, nullable=False)  # RAM in MB
    cpu_cores = db.Column(db.Integer, nullable=False)  # Number of CPU cores
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(50), default="Inactive")  # Status can be Inactive, Active, or Terminated
    
    def __repr__(self):
        return f'<Cluster {self.name} - Status: {self.status}>'
