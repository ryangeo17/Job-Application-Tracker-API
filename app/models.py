from app.db import db
from datetime import datetime
class Company(db.Model):
    __tablename__= "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f"<Company(id={self.id}, name={self.name})>"
    

class Application(db.Model):
    __tablename__= "applications"

    id=db.Column(db.Integer, primary_key=True)
    company_id=db.Column(db.Integer, db.ForeignKey("company.id"))
    role=db.Column(db.String(100), nullable=False)
    applied=db.Column(db.Boolean, default=False)
    applied_at=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Application(id={self.id}, name={self.role})>"
