from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models import db, Employee, Users, Team
from datetime import datetime

routes = Blueprint("routes", __name__)

# ----------------- USER LOGIN -----------------
@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = Users.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    if check_password_hash(user.password, password):
        return jsonify({"message": "Login successful", "role": user.role})

    return jsonify({"error": "Invalid password"}), 401

# ----------------- EMPLOYEE CRUD -----------------
@routes.route("/employees", methods=["GET"])
def get_employees():
    all_employees = Employee.query.all()
    return jsonify([
        {
            "id": e.id,
            "employee_id": e.employee_id,
            "full_name": e.full_name,
            "email": e.email,
            "phone": e.phone,
            "department": e.department,
            "role": e.role,
            "status": e.status
        } for e in all_employees
    ])

@routes.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({
        "id": emp.id,
        "employee_id": emp.employee_id,
        "full_name": emp.full_name,
        "email": emp.email,
        "phone": emp.phone,
        "dob": emp.dob.strftime("%Y-%m-%d") if emp.dob else None,
        "gender": emp.gender,
        "department": emp.department,
        "status": emp.status,
        "role": emp.role,
        "joining_date": emp.joining_date.strftime("%Y-%m-%d") if emp.joining_date else None,
        "salary": emp.salary,
        "employment_type": emp.employment_type,
        "work_location": emp.work_location,
        "emergency_name": emp.emergency_name,
        "emergency_phone": emp.emergency_phone,
        "emergency_email": emp.emergency_email,
        "emergency_relation": emp.emergency_relation
    })

@routes.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        new_employee = Employee(
            employee_id=data.get("employeeId"),
            full_name=data.get("fullName"),
            email=data.get("email"),
            phone=data.get("phone"),
            dob=datetime.strptime(data.get("dob"), "%Y-%m-%d") if data.get("dob") else None,
            gender=data.get("gender"),
            department=data.get("department"),
            role=data.get("role"),
            joining_date=datetime.strptime(data.get("joiningDate"), "%Y-%m-%d") if data.get("joiningDate") else None,
            salary=float(data.get("salary")) if data.get("salary") else None,
            employment_type=data.get("employmentType"),
            work_location=data.get("workLocation"),
            emergency_name=data.get("emergencyName"),
            emergency_phone=data.get("emergencyPhone"),
            emergency_email=data.get("emergencyEmail"),
            emergency_relation=data.get("emergencyRelation"),
            status="Active"
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({"message": "Employee added successfully!"}), 201
    except Exception as e:
        print("Error adding employee:", e)
        return jsonify({"error": "Failed to add employee"}), 500

@routes.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    emp.employee_id = data.get("employeeId", emp.employee_id)
    emp.full_name = data.get("fullName", emp.full_name)
    emp.email = data.get("email", emp.email)
    emp.phone = data.get("phone", emp.phone)
    emp.dob = datetime.strptime(data.get("dob"), "%Y-%m-%d") if data.get("dob") else emp.dob
    emp.gender = data.get("gender", emp.gender)
    emp.department = data.get("department", emp.department)
    emp.role = data.get("role", emp.role)
    emp.joining_date = datetime.strptime(data.get("joiningDate"), "%Y-%m-%d") if data.get("joiningDate") else emp.joining_date
    emp.salary = float(data.get("salary")) if data.get("salary") else emp.salary
    emp.employment_type = data.get("employmentType", emp.employment_type)
    emp.work_location = data.get("workLocation", emp.work_location)
    emp.emergency_name = data.get("emergencyName", emp.emergency_name)
    emp.emergency_phone = data.get("emergencyPhone", emp.emergency_phone)
    emp.emergency_email = data.get("emergencyEmail", emp.emergency_email)
    emp.emergency_relation = data.get("emergencyRelation", emp.emergency_relation)
    emp.status = data.get("status", emp.status)

    db.session.commit()
    return jsonify({"message": "Employee updated successfully"})

@routes.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully"})

# ----------------- TEAM ROUTES -----------------
@routes.route("/teams", methods=["POST"])
def create_team():
    data = request.get_json()
    team_name = data.get("name")
    project = data.get("project")
    lead_id = data.get("lead_id")
    member_ids = data.get("member_ids", [])

    new_team = Team(name=team_name, project=project, lead_id=lead_id)

    # Add members to the team
    for emp_id in member_ids:
        emp = Employee.query.get(emp_id)
        if emp:
            new_team.members.append(emp)

    db.session.add(new_team)
    db.session.commit()

    return jsonify({"message": "Team created successfully"}), 201

@routes.route("/teams", methods=["GET"])
def get_teams():
    teams = Team.query.all()
    output = []
    for t in teams:
        output.append({
            "id": t.id,
            "name": t.name,
            "project": t.project,
            "lead": {"id": t.lead.id, "full_name": t.lead.full_name} if t.lead else None,
            "members": [{"id": m.id, "full_name": m.full_name} for m in t.members]
        })
    return jsonify(output)
