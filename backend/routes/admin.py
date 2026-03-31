from flask import Blueprint, request, jsonify

admin_bp = Blueprint('admin', __name__)

levels = []  # In-memory storage for levels
submissions = []  # In-memory storage for submissions

@admin_bp.route('/admin/levels', methods=['POST'])
def create_level():
    new_level = request.json  # Expect level data in JSON format
    levels.append(new_level)
    return jsonify(new_level), 201

@admin_bp.route('/admin/levels', methods=['GET'])
def get_levels():
    return jsonify(levels), 200

@admin_bp.route('/admin/submissions', methods=['POST'])
def create_submission():
    new_submission = request.json  # Expect submission data in JSON format
    submissions.append(new_submission)
    return jsonify(new_submission), 201

@admin_bp.route('/admin/submissions', methods=['GET'])
def get_submissions():
    return jsonify(submissions), 200
