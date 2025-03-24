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
