#!/usr/bin/env python3

from flask import Blueprint, jsonify
from models import Project

# Create a Blueprint for projects routes
projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    """
    Fetch all projects from the database and return them as JSON.
    """
    try:
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
        return jsonify(projects_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
