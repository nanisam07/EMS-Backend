from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):  # plural name to match your app.py
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   

    # Employee Info
    employee_id = db.Column(db.String(50), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(20), default="Active", nullable=False)

    # Job Details
    department = db.Column(db.String(50))
    role = db.Column(db.String(50))
    joining_date = db.Column(db.Date)
    salary = db.Column(db.Float)
    employment_type = db.Column(db.String(20))
    work_location = db.Column(db.String(50))

    # Emergency Contact
    emergency_name = db.Column(db.String(100))
    emergency_phone = db.Column(db.String(20))
    emergency_email = db.Column(db.String(100))
    emergency_relation = db.Column(db.String(50))

#For Team Management
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    project = db.Column(db.String(100))
    lead_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    lead = db.relationship("Employee", foreign_keys=[lead_id])
    members = db.relationship(
        "Employee",
        secondary="team_members",  # This points to the association table
        backref=db.backref("teams", lazy="dynamic")
    )

team_members = db.Table(
    "team_members",
    db.Column("team_id", db.Integer, db.ForeignKey("team.id"), primary_key=True),
    db.Column("employee_id", db.Integer, db.ForeignKey("employee.id"), primary_key=True),
)




