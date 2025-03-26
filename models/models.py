# from .database import db
from config.settings import db

class GigiCmsLogin(db.Model):
  __tablename__ = 'gigicmslogin'  # Table name in the database
  gl_recid = db.Column(db.Integer, primary_key=True)
  gl_username = db.Column(db.String(100), nullable=False)
  gl_password = db.Column(db.String(100), nullable=False)
  gl_role = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"gigicmslogin ('{self.gl_recid}', '{self.gl_username}', '{self.gl_password}')"
# GL_USERNAME	varchar


class hms_doctor(db.Model):
   __tablename__ = 'hms_doctor'
   dr_recid = db.Column(db.Integer, primary_key=True, autoincrement=True)
   dr_firstname = db.Column(db.String(100), nullable=False)
   dr_lastname = db.Column(db.String(100), nullable=False)
   dr_globalid = db.Column(db.String(50), nullable=False)
   dr_emailid = db.Column(db.String(50), nullable=False)
   dr_phonenumber = db.Column(db.String(20), nullable=False)
   dr_alternatephone = db.Column(db.String(20), nullable=False)
   dr_qualification = db.Column(db.String(100), nullable=False)
   dr_specialqualification = db.Column(db.String(100), nullable=False)
   dr_dateofbirth = db.Column(db.Date, nullable=False)
   dr_dateofjoining = db.Column(db.Date, nullable=False)

   def __repr__(self):
      return f"hms_doctor ('{self.dr_recid}', '{self.dr_firstname}', '{self.dr_lastname}')"

class resulttable(db.Model):
      r_recid = db.Column(db.Integer, primary_key=True)
      r_code = db.Column(db.String(10), nullable=False)
      r_message = db.Column(db.String(255), nullable=False)

class errortable(db.Model):
    e_recid = db.Column(db.Integer, primary_key=True)
    e_code = db.Column(db.String(10), nullable=False)
    e_description = db.Column(db.String(250), nullable=False)
    e_systemerrormessage = db.Column(db.String(255), nullable=False)

class hms_patient(db.Model):
   __tablename__ = 'hms_patient'
   pa_recid = db.Column(db.Integer, primary_key=True, autoincrement=True)
   pa_firstname = db.Column(db.String(100), nullable=False)
   pa_lastname = db.Column(db.String(100), nullable=False)
   pa_emailid = db.Column(db.String(50), nullable=False)
   pa_phonenumber = db.Column(db.String(20), nullable=False)
   pa_alternatephone = db.Column(db.String(20), nullable=False)
   pa_dateofbirth = db.Column(db.Date, nullable=False)
   pa_dateofjoining = db.Column(db.Date, nullable=False) 