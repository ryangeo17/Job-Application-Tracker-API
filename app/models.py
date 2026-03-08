from app.db import db
from datetime import datetime
    

class Application(db.Model):
    __tablename__= "applications"

    id=db.Column(db.Integer, primary_key=True)
    company=db.Column(db.String(100), nullable=False)
    role=db.Column(db.String(100), nullable=False)
    applied=db.Column(db.Boolean, default=False)
    applied_at=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Application(id={self.id}, role={self.role})>"
