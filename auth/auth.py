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
