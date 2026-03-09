from flask import Blueprint, request, jsonify
from app.db import db
from app.models import Application
bp = Blueprint("applications", __name__)

VALID_STATUSES = {"applied", "interview", "offer", "rejected"}

#GET operations
@bp.route("/applications", methods=['GET'])
def get_applications():
    query = Application.query

    status = request.args.get("status")
    if status and status not in VALID_STATUSES:
        return {"error": "Invalid status filter"}, 400
    sort = request.args.get("sort")

    #filter by status
    if status:
        query = query.filter_by(status=status)

    #sort by application date
    if sort == "applied_at":
        query = query.order_by(Application.applied_at)
    elif sort == "-applied_at":
        query = query.order_by(Application.applied_at.desc())

    #limiting and offsetting
    limit = request.args.get("limit", type=int)
    offset = request.args.get("offset", type=int)

    if limit:
        query = query.limit(limit)

    if offset:
        query = query.offset(offset)

        apps = query.all()

        return jsonify([a.to_dict() for a in apps])


@bp.route("/applications/<int:id>", methods=["GET"])
def get_application(id):
    application = Application.query.get_or_404(id)
    return jsonify(application.to_dict())

#POST operations

@bp.route("/applications", methods=["POST"])
def add_application():
    data = request.get_json()
    if not data:
        return {"error": "Request body must be JSON"}, 400

    company = data.get("company")
    role = data.get("role")
    status = data.get("status", "applied")

    if not company or not role:
        return {"error": "company and role are required"}, 400

    if not status:
        return {"error": "status is required"}, 400


    if status not in VALID_STATUSES:
        return {"error": "Invalid status"}, 400

    new_application = Application(
        company=company,
        role=role,
        status=status,
    )

    db.session.add(new_application)
    db.session.commit()

    return jsonify(new_application.to_dict()), 201

#PUT operations



@bp.route("/applications/<int:id>", methods=["PUT"])
def update_application(id):
    application = Application.query.get_or_404(id)
    data = request.get_json()

    status = data.get("status")

    if status not in VALID_STATUSES:
        return {"error": "Invalid status"}, 400

    application.status = status
    db.session.commit()

    return jsonify(application.to_dict())

#DELETE operations

@bp.route("/applications/<int:id>", methods=["DELETE"])
def delete_application(id):
    application = Application.query.get_or_404(id)

    db.session.delete(application)
    db.session.commit()

    return {"message": "Application deleted"}

@bp.route("/applications", methods=["DELETE"])
def delete_by_status():
    status = request.args.get("status")

    if status not in VALID_STATUSES:
        return {"error": "Provide valid status"}, 400

    #filtering by status
    Application.query.filter_by(status=status).delete()
    db.session.commit()

    return {"message": f"Deleted all {status} applications"}