from flask import Flask, request, jsonify
from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import os
import avjoService
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"  # Use SQLite for simplicity
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    contact = db.Column(db.String(120), unique=True, nullable=False)
    context = db.Column(db.Text)

    def __repr__(self):
        return f"<User {self.username}>"


@app.route("/user", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(
        username=data["username"],
        address=data["address"],
        contact=data.get("contact", ""),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully!"})


@app.route("/users", methods=["GET"])
def get_all_users():
    users = User.query.all()
    return jsonify(
        [
            {
                "id": user.id,
                "username": user.username,
                "address": user.address,
                "context": user.context,
                "contact": user.contact,
            }
            for user in users
        ]
    )


@app.route("/user/context/<int:user_id>", methods=["PUT"])
def update_user_context(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found!"}), 404

    data = request.get_json()
    user.context = data["context"]
    db.session.commit()
    return jsonify({"message": "User context updated successfully!"})


@app.route("/checkDoc", methods=["POST"])
def checkDoc():
    """Check if the documents are uploaded or not"""
    # Check for required headers
    if (
        "Content-Type" not in request.headers
        or request.headers["Content-Type"] != "application/json"
    ):
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if "user id" not in args:
        return jsonify({"error": "Missing 'user id' in request body"}), 400

    result = avjoService.checkDocService(args["user id"])

    return jsonify("No documents Uploaded")


@app.route("/getContext", methods=["POST"])
def getContext():
    """Returns the context from the documents uploaded"""

    # Check for required headers
    if (
        "Content-Type" not in request.headers
        or request.headers["Content-Type"] != "application/json"
    ):
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if "user id" not in args:
        return jsonify({"error": "Missing 'user id' in request body"}), 400

    context = avjoService.getContextService(args["user id"])

    return jsonify(context)


@app.route("/checkFraud", methods=["POST"])
def checkFraud():
    """Check from the RAG model if its a fraud and then conversate with user"""
    # Check for required headers
    if (
        "Content-Type" not in request.headers
        or request.headers["Content-Type"] != "application/json"
    ):
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    if "situation" not in args:
        return jsonify({"error": f"Missing situation in request body"}), 400

    fraudContext = avjoService.checkFraudService(args["situation"])

    return jsonify("This has happened before its a fraud i see")


@app.route("/triggerEmail", methods=["POST"])
def triggerEmail():
    """Generate and Trigger Email of Cyber Department"""
    # Check for required headers
    if (
        "Content-Type" not in request.headers
        or request.headers["Content-Type"] != "application/json"
    ):
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]
    # name, address, contact number, awb number, breif overview of situation
    req_inp = ["user name", "address", "contact no", "situation"]

    for inp in req_inp:
        if inp not in args:
            return jsonify({"error": f"Missing {inp} in request body"}), 400  
        
    avjoService.triggerEmailService(args["user name"], args["address"],args["contact no"],args["situation"])

@app.route('/generateReport', methods=['POST'])
def generateReport():
    """Generate a Report of the fraud & store it in DB"""
    # Check for required headers
    if (
        "Content-Type" not in request.headers
        or request.headers["Content-Type"] != "application/json"
    ):
        return jsonify({"error": "Content-Type must be application/json"}), 400

    # Get input from body
    data = request.json
    args = data["args"]

    return jsonify("Report generate check DB")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This creates the database tables
    app.run(debug=True)
