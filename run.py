"""Application entry point"""
import os
from app import create_app, db
from app.models import Record # Import model to ensure it's loaded for migrations

# Create app instance
app = create_app()

# CLI command to initialize database
@app.cli.command()
def init_db():
    """Create database tables"""
    # This function is simpler now, relying on SQLAlchemy to create tables
    db.create_all()
    print('Database initialized.')

# Ensures 'app' is available for the 'flask' command (e.g., flask db migrate)
if __name__ == '__main__':
    # Flask recommends running the app via 'flask run' in production, 
    # but this is fine for development.
    app.run(debug=True)