from flask import request, jsonify
from config.settings import db
from models.models import hms_patient, resulttable, errortable  # Import the updated User model

def post_patient():
 
    try:
        
        data = request.get_json()
        pa_firstname = data.get('FirstName')
        pa_lastname = data.get('LastName')
        pa_emailid = data.get('EmailId')
        pa_phonenumber = data.get('PhoneNumber')
        pa_alternatephone = data.get('AlternatePhone')
        pa_dateofbirth = data.get('DateOfBirth')
        pa_dateofjoining = data.get('DateOfJoining')
        
        new_patient = hms_patient(pa_firstname=pa_firstname, pa_lastname=pa_lastname, pa_emailid=pa_emailid, 
                                 pa_phonenumber=pa_phonenumber, pa_alternatephone=pa_alternatephone,
                                 pa_dateofbirth=pa_dateofbirth, pa_dateofjoining=pa_dateofjoining
                                ) 
        
            # Add doctor to the session and commit to the database
        db.session.add(new_patient)
        db.session.commit()
        result = resulttable.query.filter_by(r_recid=100).first()
        return jsonify({'status':'Y', 'message': result.r_message})
    except Exception as e:
        db.session.rollback()  # Rollback if error occurs
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) 
def getall_patient():  
    try:
        patients = hms_patient.query.all()
        return jsonify({'status':'Y', 'data':[user_to_dict(doc) for doc in patients]})       
    except Exception as e:
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) ,400
def user_to_dict(hms_patient):
    return {
            "RecordId": hms_patient.dr_recid,
            "FirstName": hms_patient.dr_firstname,
            "LastName": hms_patient.dr_lastname,
            "EmailId": hms_patient.dr_emailid,
            "PhoneNumber": hms_patient.dr_phonenumber,
            "AlternatePhone": hms_patient.dr_alternatephone,
            "DateOfBirth": hms_patient.dr_dateofbirth,
            "DateOfJoining": hms_patient.dr_dateofjoining
    }

def get_patient(pa_recid):
    try:
        if pa_recid ==0:
            patient_data= {
        "RecordId": "",
        "FirstName": "",
        "LastName": "",
        "EmailId": "",
        "PhoneNumber": "",
        "AlternatePhone": "",
        "DateOfBirth": "",
        "DateOfJoining": ""
         }  
            return jsonify({'status': 'Y', 'data': patient_data}), 200

        patient = hms_patient.query.filter_by(pa_recid=pa_recid).first()
        if not patient:
            return jsonify({'status': 'N', 'message': 'Patient not found'}), 404
        return jsonify({'status': 'Y', 'data': user_to_dict(patient)}), 200
        
    except Exception as e:
        # errortable(str(e), traceback.format_exc(), 'some_system_error_message')  # Log the error details
        error = errortable.query.filter_by(e_recid=401).first()
        return jsonify({'status':'N', 'message': error.e_description, 'error':str(e)}) ,400

def user_to_dict(patient):
    return {
        "RecordId": patient.pa_recid,
        "FirstName": patient.pa_firstname,
        "LastName": patient.pa_lastname,
        "EmailId": patient.pa_emailid,
        "PhoneNumber": patient.pa_phonenumber,
        "AlternatePhone": patient.pa_alternatephone,
        "DateOfBirth": patient.pa_dateofbirth,
        "DateOfJoining": patient.pa_dateofjoining
    }

def update_patient(pa_recid):    
    data = request.get_json()  # Get the JSON data from the request    
    # Extract fields from incoming data
    pa_firstname = data.get('FirstName')
    pa_lastname = data.get('LastName')
    pa_emailid = data.get('EmailId')
    pa_phonenumber = data.get('PhoneNumber')
    pa_alternatephone = data.get('AlternatePhone')
    pa_dateofbirth = data.get('DateOfBirth')
    pa_dateofjoining = data.get('DateOfJoining')
        
    try:
        # Fetch the existing patient record by RECORDID
        patient = hms_patient.query.get(pa_recid)        
        if patient:
            # Update the fields of the existing patient record
            patient.pa_firstname = pa_firstname
            patient.pa_lastname = pa_lastname
            patient.pa_emailid = pa_emailid
            patient.pa_phonenumber = pa_phonenumber
            patient.pa_alternatephone = pa_alternatephone
            patient.pa_dateofbirth = pa_dateofbirth
            patient.pa_dateofjoining = pa_dateofjoining
                      
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

# 5. Delete: Delete patient by RECORDID
def delete_patient(pa_recid):
    
    try:
        patient = hms_patient.query.get(pa_recid)  # Fetch the doctor by ID
        if patient:
            db.session.delete(patient)  # Delete the doctor
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