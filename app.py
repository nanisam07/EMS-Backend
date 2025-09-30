from flask import Flask
from flask_cors import CORS
from models import db, Users
from routes import routes
from werkzeug.security import generate_password_hash
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

# ----------------- DB Config -----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Register routes
app.register_blueprint(routes)

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

if __name__ == '__main__':
    with app.app_context():
        init_users()  # only inserts if table already exists
    app.run(host="0.0.0.0", port=5000, debug=True)
