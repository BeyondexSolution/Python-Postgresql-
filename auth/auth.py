import jwt
import os
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Get the token from the request headers
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split("Bearer ")[-1]  # Extract token after "Bearer "

        if not token:
            return jsonify({"status": "N", "msg": "Token is missing!"}), 401

        try:
            # Decode JWT token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = data  # Store user info in request context
        except jwt.ExpiredSignatureError:
            return jsonify({"status": "N", "msg": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"status": "N", "msg": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated

AuthroziationKey="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiODFlMTVlODVmZDhmYzMxMzk3NWY3MGNiODEwMjc3YWVhODRmODlkNjc4Y2I0ZDFkNTM2NGUyMjFlNWY4YzMxODQyYmYyMjY4MmJkMDYyZGMiLCJpYXQiOjE3MjI1MTk3NDAuMTk2OTg1LCJuYmYiOjE3MjI1MTk3NDAuMTk2OTk2LCJleHAiOjE3NTQwNTU3NDAuMTUyOTYzLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.F4lOKPPewIKjbJKK-HPgBfK_mnG2Rzw4AUv4w87HGXLSXl3GYfGurHAlTriVQ-KkpOftCv_QGDDflCB2MG4D0bV6rcGsD7Ayvr40yk_m3Fyz1AhB2w70Y7gMpfhd_3hEDNWZ-V9lAgH24s-UCdFqKFwZkd9icQ84NfRij9bay3M7mjJ_KR06-cfuVMGhZFGnw89jiFr5FDt1DpWeqzAOjFIBtCfywV0CvNFMJtDrNvtjAzRAbR0vDVaXZBk0xa6aMyxBhhFX4fC9FaRAU15a9oQh2RH4OheNOvqH54v32BBXHx305g-S1DLYXQWlPUZROoTiaDrJezHPog3QKZlC3J7cscLIt-nd4XlYVe9ntMOGk7rzXvEAhcai1-yTkHZZfNfy7EIifi0hXcJrR9NbRjdloPjfGCo3BsH425V3PhUyr_OaC9KxxUHHLwmEnyCWlFIfAzyMpC9g7NqpSVDYcVt--mzxGkdY6_PF-g0e43h9d1g8uxbD6iZtLVAejpsmqoEWaJxKJNrESLiYOoYu0QFGFl46bkbuTwhepswe5Pwjs54S-ps7DB2igPgT9rABF-eotflzG-zruLGQNSO-fjRY5KjSE97n2W348DKjPxHF3U1q9BW2KhGAdb-h4bOKOT6Lu4cpN7v1eRnMxucEZV3a5kIrWc2xg-7H_s3zXi4"

def check_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Get the token from the request headers
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split("Bearer ")[-1]  # Extract token after "Bearer "

        if not token:
            return jsonify({"status": "N", "msg": "Please provide Authorization"}), 401

        if token!=AuthroziationKey:
                return jsonify({"status": "N", "msg": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated

