from flask import Flask, jsonify
from flask_cors import CORS
from models import db, Users
from routes import routes
from werkzeug.security import generate_password_hash
from flask_migrate import Migrate
import os

# ----------------- Flask App -----------------
app = Flask(__name__)
CORS(app)  # Allow all origins for now

# ----------------- DB Config -----------------
# Use SQLite locally or switch to PostgreSQL in production
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# ----------------- Register Blueprint -----------------
app.register_blueprint(routes)

# ----------------- Root Route -----------------
@app.route("/")
def home():
    return jsonify({"message": "Backend is live!"})

# ----------------- Initialize Default Users -----------------
def init_users():
    if not Users.query.first():
        users = [
            {"email": "hr@example.com", "password": "hr123", "role": "hr"},
            {"email": "manager@example.com", "password": "manager123", "role": "manager"},
            {"email": "ceo@example.com", "password": "ceo123", "role": "ceo"},
        ]
        for u in users:
            hashed = generate_password_hash(u["password"], method="pbkdf2:sha256")
            db.session.add(Users(email=u["email"], password=hashed, role=u["role"]))
        db.session.commit()
        print("Default users initialized.")

# ----------------- Main -----------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not exist
        init_users()     # Insert default users
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
