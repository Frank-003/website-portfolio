#!/usr/bin/env python3

import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Enable CORS
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Import models
from models import Contact, Project


# Serve frontend files
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# API to submit contact form
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([name, email, subject, message]):
        return jsonify({'error': 'All fields are required!'}), 400

    new_contact = Contact(name=name, email=email, subject=subject, message=message)
    db.session.add(new_contact)
    db.session.commit()

    return jsonify({'message': 'Your message has been sent successfully!'})

# API to get projects
@app.route('/projects', methods=['GET'])
def projects():
    projects = Project.query.all()
    projects_list = [
        {
            "id": project.id,
            "title": project.title,
            "link": project.link,
            "description": project.description,
        }
        for project in projects
    ]
    return jsonify(projects_list)

if __name__ == '__main__':
    # Create database tables if not exist
    if not os.path.exists('database.db'):
        db.create_all()

    # Run the app
    app.run(debug=True)
    # Run the app
    app.run(debug=True)
