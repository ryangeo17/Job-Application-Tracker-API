from app.db import db
from datetime import datetime
    

class Application(db.Model):
    __tablename__= "applications"

    id=db.Column(db.Integer, primary_key=True)
    company=db.Column(db.String(100), nullable=False)
    role=db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="applied")
    applied_at=db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "role": self.role,
            "status": self.status,
            "applied_at": self.applied_at
        }
    def __repr__(self):
        return f"<Application(id={self.id}, role={self.role})>"
