from flask import Blueprint, request, jsonify

# Create a blueprint for leaderboard routes
leaderboard_bp = Blueprint('leaderboard', __name__)

# Sample player data
players = [
    {'username': 'player1', 'total_points': 150},
    {'username': 'player2', 'total_points': 200},
    {'username': 'player3', 'total_points': 100},
]

@leaderboard_bp.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    sort_by = request.args.get('sort_by', 'total_points')  # sorting field
    order = request.args.get('order', 'asc')  # sorting order

    # Validate the sort field and order
    if sort_by not in ['total_points', 'username']:
        return jsonify({'error': 'Invalid sort_by parameter. Use total_points or username.'}), 400
    if order not in ['asc', 'desc']:
        return jsonify({'error': 'Invalid order parameter. Use asc or desc.'}), 400

    # Sort players
    sorted_players = sorted(players, key=lambda x: x[sort_by])
    if order == 'desc':
        sorted_players.reverse()

    return jsonify(sorted_players)  # Return sorted player data
