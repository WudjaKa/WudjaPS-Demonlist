import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')


@app.route('/admin/login', methods=['POST'])
def admin_login():
    json_data = request.get_json()
    password = json_data.get('password')
    if password == ADMIN_PASSWORD:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid password'}), 401


# Existing endpoints for creating and getting levels and submissions remain unchanged.

@app.route('/levels', methods=['POST'])
def create_level():
    # Your existing code here
    pass

@app.route('/levels', methods=['GET'])
def get_levels():
    # Your existing code here
    pass

@app.route('/submissions', methods=['POST'])
def create_submission():
    # Your existing code here
    pass

@app.route('/submissions', methods=['GET'])
def get_submissions():
    # Your existing code here
    pass
