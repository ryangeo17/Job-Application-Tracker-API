from flask import request,jsonify
from app.db import db
from run import app
from app.models import Application

@app.route("/applications", methods=['GET'])
def get_applications():
    apps= Application.query.all()
    result=[]
    for a in apps:
        result.append({
            "id": a.id,
            "company": a.company,
            "role": a.role,
            "applied": a.applied,
            "applied_at":a.applied_at,
        })
    return jsonify(result)

@app.route("/applications", methods=['POST'])
def add_application():
    data=request.get_json()
    new_application = Application(
        company=data["company"],
        role=data["role"],
        applied=data["applied"],
    )
    db.session.add(new_application)
    db.session.commit()

    return jsonify({
        "id": new_application.id,
        "company": new_application.company,
        "role": new_application.role,
        "applied": new_application.applied,
        "applied_at": new_application.applied_at
    }), 201


@app.route("/applications/<int:id>", methods=['PUT'])
def update_application(id):
    application=Application.query.get_or_404(id)
    data=request.get_json()
    application.applied=data["applied"]
    db.session.commit()

    return jsonify({"message":"Application has been updated."})


@app.route("/applications/<int:id>", methods=['DELETE'])
def delete_application(id):
    application=Application.query.get_or_404(id)
    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application has been deleted"})

    