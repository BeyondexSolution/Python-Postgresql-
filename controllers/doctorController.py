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
        return jsonify({'status':'Y', 'message': result.r_message})
    except Exception as e:
        db.session.rollback()  # Rollback if error occurs
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) 
def getall_doctor():  
    try:
        doctors = hms_doctor.query.all()
        return jsonify({'status':'Y', 'data':[user_to_dict(doc) for doc in doctors]})       
    except Exception as e:
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) ,400
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

def get_doctor(dr_recid):
    try:
        doctor = hms_doctor.query.filter_by(dr_recid=dr_recid).first()
        if not doctor:
            return jsonify({'status': 'N', 'message': 'Doctor not found'}), 404
        return jsonify({'status': 'Y', 'data': user_to_dict(doctor)}), 200
    except Exception as e:
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) ,400

def user_to_dict(doctor):
    return {
        "RecordId": doctor.dr_recid,
        "FirstName": doctor.dr_firstname,
        "LastName": doctor.dr_lastname,
        "GlobalId": doctor.dr_globalid,
        "EmailId": doctor.dr_emailid,
        "PhoneNumber": doctor.dr_phonenumber,
        "AlternatePhone": doctor.dr_alternatephone,
        "Qualification": doctor.dr_qualification,
        "SpecialQualification": doctor.dr_specialqualification,
        "DateOfBirth": doctor.dr_dateofbirth,
        "DateOfJoining": doctor.dr_dateofjoining
    }

def update_doctor(dr_recid):
    # Check for valid API key (authentication)
    # auth_error = check_api_key()
    # if auth_error:
    #     return auth_error  # Ensure this returns a valid response    
    data = request.get_json()  # Get the JSON data from the request    
    # Extract fields from incoming data
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
        
    try:
        # Fetch the existing doctor record by RECORDID
        doctor = hms_doctor.query.get(dr_recid)        
        if doctor:
            # Update the fields of the existing doctor record
            doctor.dr_firstname = dr_firstname
            doctor.dr_lastname = dr_lastname
            doctor.dr_globalid = dr_globalid
            doctor.dr_emailid = dr_emailid
            doctor.dr_phonenumber = dr_phonenumber
            doctor.dr_alternatephone = dr_alternatephone
            doctor.dr_qualification = dr_qualification
            doctor.dr_specialqualification = dr_specialqualification
            doctor.dr_dateofbirth = dr_dateofbirth
            doctor.dr_dateofjoining = dr_dateofjoining
                      
            db.session.commit()  # Commit the changes to the database
            result = resulttable.query.filter_by(r_recid=200).first()
            return jsonify({'status':'Y', 'message': result.r_message})  # Return success message
        else:
            # If record doesn't exist, return a 404 not found error
            return jsonify({'message': 'doctor record not found'})    
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        # ERRORTABLE(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)})

# 5. Delete: Delete doctor by RECORDID
def delete_doctor(dr_recid):
    # Check for valid API key
    # auth_error = check_api_key()
    # if auth_error:
    #     resulttable('delete_doctor', 'failed', 'Unauthorized access attempt')
    #     return auth_error
    try:
        doctor = hms_doctor.query.get(dr_recid)  # Fetch the doctor by ID
        if doctor:
            db.session.delete(doctor)  # Delete the doctor
            db.session.commit()  # Commit the changes
            # RESULTTABLE('get_doctor', 'success')
            result = resulttable.query.filter_by(r_recid=300).first()
            return jsonify({'status':'Y','message': result.r_message})
        else:    
         # If record doesn't exist, return a 404 not found error
            return jsonify({"message": "Doctor record not found"})    
    except Exception as e:
        db.session.rollback()  # Rollback if error occurs
        # ERRORTABLE(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)})
