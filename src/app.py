# src/app.py
from flask import Flask
from .config import Config
from .database import db  # Import db from database module
from .controllers.quiz_controller import quiz_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize the SQLAlchemy database with the app
    db.init_app(app)
    
    # Register the Quiz Blueprint
    app.register_blueprint(quiz_bp)

    # Create the tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
