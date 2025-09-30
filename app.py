from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, Users
from routes import routes
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

app = Flask(__name__)
CORS(app)  # Allow all origins. You can restrict later if needed

# ----------------- DB Config -----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Or use PostgreSQL for production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Register routes
app.register_blueprint(routes)

@app.route("/")
def home():
    return jsonify({"message": "Backend is live!"})

# ----------------- Initialize Users -----------------
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

# ----------------- Login Route -----------------
@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = Users.query.filter_by(email=data.get("email")).first()
    if user and check_password_hash(user.password, data.get("password")):
        return jsonify({"role": user.role})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        init_users()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
