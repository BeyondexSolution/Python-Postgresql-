from flask import Blueprint,jsonify
from controllers import userController  # Example controller
from auth.auth import token_required

routes_bp = Blueprint('routes', __name__)
@routes_bp.route('/')
def home():
    return "Hello, Flask with MSSQL!"

@routes_bp.route("/login", methods=["POST"])
def get_users():
    return userController.login()

@routes_bp.route('/users', methods=['GET'])
@token_required 
def get_userdata():
    user_data = userController.get_all_users()
    return jsonify(user_data)
# Add more routes here
