from flask import Blueprint, request, jsonify
from app import db
from models import Level

levels_bp = Blueprint('levels', __name__, url_prefix='/api/levels')

@levels_bp.route('/', methods=['GET'])
def get_all_levels():
    """Fetch all levels sorted by position"""
    levels = Level.query.order_by(Level.position).all()
    return jsonify([{
        'id': level.id,
        'name': level.name,
        'difficulty': level.difficulty,
        'points': level.points,
        'position': level.position
    } for level in levels])

@levels_bp.route('/<int:level_id>', methods=['GET'])
def get_level(level_id):
    """Fetch a specific level by ID"""
    level = Level.query.get(level_id)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    return jsonify({
        'id': level.id,
        'name': level.name,
        'difficulty': level.difficulty,
        'points': level.points,
        'position': level.position
    })

@levels_bp.route('/', methods=['POST'])
def create_level():
    """Create a new level (admin only)"""
    data = request.json
    if not data.get('name') or data.get('difficulty') is None or data.get('points') is None:
        return jsonify({'error': 'Missing required fields'}), 400
    
    new_level = Level(
        name=data['name'],
        difficulty=data['difficulty'],
        points=data['points'],
        position=data.get('position', Level.query.count() + 1)
    )
    db.session.add(new_level)
    db.session.commit()
    
    return jsonify({
        'id': new_level.id,
        'name': new_level.name,
        'difficulty': new_level.difficulty,
        'points': new_level.points,
        'position': new_level.position
    }), 201

@levels_bp.route('/<int:level_id>', methods=['PUT'])
def update_level(level_id):
    """Update a level (admin only)"""
    level = Level.query.get(level_id)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    
    data = request.json
    if 'name' in data:
        level.name = data['name']
    if 'difficulty' in data:
        level.difficulty = data['difficulty']
    if 'points' in data:
        level.points = data['points']
    if 'position' in data:
        level.position = data['position']
    
    db.session.commit()
    return jsonify({
        'id': level.id,
        'name': level.name,
        'difficulty': level.difficulty,
        'points': level.points,
        'position': level.position
    })

@levels_bp.route('/<int:level_id>', methods=['DELETE'])
def delete_level(level_id):
    """Delete a level (admin only)"""
    level = Level.query.get(level_id)
    if not level:
        return jsonify({'error': 'Level not found'}), 404
    
    db.session.delete(level)
    db.session.commit()
    return jsonify({'message': 'Level deleted successfully'})
