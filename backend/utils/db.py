# utils/db.py

from models import db

def commit_changes():
    """Commit the current database transaction."""
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

def add_record(record):
    """Add a new record to the database."""
    db.session.add(record)
    commit_changes()

def delete_record(record):
    """Delete a record from the database."""
    db.session.delete(record)
    commit_changes()
