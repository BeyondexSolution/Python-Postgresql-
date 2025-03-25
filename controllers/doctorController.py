from flask import request, jsonify
from config.settings import db
from models.models import hms_doctor, resulttable, errortable  # Import the updated User model
from config.settings import check_api_key

def post_doctor():
  # Check for valid API key
    try:
        # auth_error = check_api_key()
        # if auth_error:
        #     resulttable('post_doctor', 'failed', 'Unauthorized access attempt')
        #     return auth_error  
        data = request.get_json()
        dr_firstname = data.get('FirstName')
        dr_lastname = data.get('LastName')
        dr_globalid = data.get('GlobalId')
        dr_emailid = data.get('EmailId')
        dr_phonenumber = data.get('PhoneNumber')
        dr_alternatephone = data.get('AlternatePhone')
        dr_qualification = data.get('Qualification')
        dr_specialqualification = data.get('SpecialQualification')
        dr_dateofbirth = data.get('DateOfBirth')
        dr_dateofjoining = data.get('DateOfJoining')
        
        new_doctor = hms_doctor(dr_firstname=dr_firstname, dr_lastname=dr_lastname, dr_globalid=dr_globalid,
                                dr_emailid=dr_emailid, dr_phonenumber=dr_phonenumber, dr_alternatephone=dr_alternatephone,
                                dr_qualification=dr_qualification, dr_specialqualification=dr_specialqualification,
                                dr_dateofbirth=dr_dateofbirth, dr_dateofjoining=dr_dateofjoining
                                ) 
        
            # Add doctor to the session and commit to the database
        db.session.add(new_doctor)
        db.session.commit()
        result = resulttable.query.filter_by(r_recid=100).first()
        return jsonify({"message": result.r_message})
    except Exception as e:
        db.session.rollback()  # Rollback if error occurs
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'message': error.e_description}) 
def getall_doctor():  
    try:
        doctors = hms_doctor.query.all()
        return jsonify({"status":"Y", "data":[user_to_dict(doc) for doc in doctors]})       
    except Exception as e:
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N','message': error.e_description, 'error':str(e)}) ,400
def user_to_dict(hms_doctor):
    return {
            "RecordId": hms_doctor.dr_recid,
            "FirstName": hms_doctor.dr_firstname,
            "LastName": hms_doctor.dr_lastname,
            "GlobalId": hms_doctor.dr_globalid,
            "EmailId": hms_doctor.dr_emailid,
            "PhoneNumber": hms_doctor.dr_phonenumber,
            "AlternatePhone": hms_doctor.dr_alternatephone,
            "Qualification": hms_doctor.dr_qualification,
            "SpecialQualification": hms_doctor.dr_specialqualification,
            "DateOfBirth": hms_doctor.dr_dateofbirth,
            "DateOfJoining": hms_doctor.dr_dateofjoining
    }
