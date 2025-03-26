from flask import Blueprint,jsonify
from controllers import patientController, userController  # Example controller
from auth.auth import token_required, check_api_key

from controllers import doctorController

routes_bp = Blueprint('routes', __name__)
@routes_bp.route('/')
def home():
    return "Hello, Flask with POSTGRESQL!"

@routes_bp.route("/login", methods=["POST"])
def get_users():
    return userController.login()

@routes_bp.route('/users', methods=['GET'])
@token_required 
def get_userdata():
    user_data = userController.get_all_users()
    return jsonify(user_data)

#--------------------DOCTOR------------------------#
@routes_bp.route('/postdoctor', methods=['POST'])
def postdoctor():
    return doctorController.post_doctor()

@routes_bp.route('/getalldoctors', methods=['GET'])
@check_api_key
def getalldoctor():
    return doctorController.getall_doctor()

@routes_bp.route('/getdoctor/<int:dr_recid>', methods=['GET'])
@check_api_key
def getdoctor(dr_recid):
    return doctorController.get_doctor(dr_recid)

@routes_bp.route('/updatedoctor/<int:dr_recid>', methods=['PUT'])
@check_api_key
def updatedoctor(dr_recid):
    return doctorController.update_doctor(dr_recid)

@routes_bp.route('/deletedoctor/<int:dr_recid>', methods=['DELETE'])
@check_api_key
def deletedoctor(dr_recid):
    return doctorController.delete_doctor(dr_recid)
#--------------------PATIENT------------------------#
@routes_bp.route('/postpatient', methods=['POST'])
def postpatient():
    return patientController.post_patient()

@routes_bp.route('/getallpatients', methods=['GET'])
@check_api_key
def getallpatient():
    return patientController.getall_patient()

@routes_bp.route('/getpatient/<int:pa_recid>', methods=['GET'])
@check_api_key
def getpatient(pa_recid):
    return patientController.get_patient(pa_recid)

@routes_bp.route('/updatepatient/<int:pa_recid>', methods=['PUT'])
@check_api_key
def updatepatient(pa_recid):
    return patientController.update_patient(pa_recid)

@routes_bp.route('/deletepatient/<int:pa_recid>', methods=['DELETE'])
@check_api_key
def deletepatient(pa_recid):
    return patientController.delete_patient(pa_recid)
