from . import db

class Notebook(db.Model):
    __tablename__ = 'notebooks'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    content = db.Column(db.Text, nullable=True)  # Stores notebook content as JSON or plain text

    def __repr__(self):
        return f'<Notebook {self.name}>'
