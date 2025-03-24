from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet
db = SQLAlchemy()  # Create an instance of SQLAlchemy
key =b'AT0yzXwZMBQ_e4Saoo-UwpFSKKhsH1_pm_rrezqDN9U='
cipher = Fernet(key)
connectionstring=b'gAAAAABn4VBfNLGTplEB4lOFSiwv_5RgXQ7QcgU79ggo7y-y451bXDIFHxe3K_bM-TFCeXMALE5l_4ZkDf6EnnXmYMrEUdvGF8ND-hJ4Dg5ymsPheTT8ZUHbqOaxaV5-ul27vbQ4dshf7WtCvjUuI65D5_JvL0xxqXyBHV41YC40_YJoTLx7xqpCncN_PB6aYTQzVUOnGHIxqf54wNvytHFUwkELNNDrRTQ9ix5ajcttcLcneSwebfVCSnKvksTp_DLD1X3XUmGq'
decrypted_uri = cipher.decrypt(connectionstring).decode()
class Config:
    SQLALCHEMY_DATABASE_URI = decrypted_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False 