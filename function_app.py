from flask import Flask
from config.settings import Config, db  # Import db from your config
from routes.routes import routes_bp

app = Flask(__name__)
app.config.from_object(Config)  # Load configurations
db.init_app(app)  # Initialize the database with the Flask app

app.register_blueprint(routes_bp)  # Register routes

# if __name__ == "__main__":
#     app.run(debug=True)

