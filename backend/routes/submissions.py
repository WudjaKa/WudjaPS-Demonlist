from flask import Blueprint, request, jsonify

submissions_bp = Blueprint('submissions', __name__)

# Dummy storage for submissions
submissions = []

@submissions_bp.route('/submissions', methods=['POST'])
def create_submission():
    data = request.json
    submission = { 'id': len(submissions) + 1, 'player_id': data['player_id'], 'status': 'pending', 'details': data['details'] }
    submissions.append(submission)
    return jsonify(submission), 201

@submissions_bp.route('/submissions/<int:submission_id>', methods=['PUT'])
def update_submission(submission_id):
    data = request.json
    for submission in submissions:
        if submission['id'] == submission_id:
            submission['status'] = data['status']
            return jsonify(submission)
    return jsonify({'error': 'Submission not found'}), 404

@submissions_bp.route('/submissions', methods=['GET'])
def fetch_submissions():
    status = request.args.get('status')
    player_id = request.args.get('player_id')
    filtered_submissions = submissions
    if status:
        filtered_submissions = [s for s in filtered_submissions if s['status'] == status]
    if player_id:
        filtered_submissions = [s for s in filtered_submissions if s['player_id'] == player_id]
    return jsonify(filtered_submissions)
