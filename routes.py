from flask import request, jsonify
from models import db, Episode, Guest, Appearance


def register_routes(app):
    
    
    @app.route('/episodes', methods=['GET'])
    def get_episodes():
        episodes = Episode.query.all()
        return jsonify([e.to_dict() for e in episodes]), 200

    
    @app.route('/episodes/<int:id>', methods=['GET'])
    def get_episode_by_id(id):
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({"error": "Episode not found"}), 404

        episode_data = episode.to_dict()
        episode_data["appearances"] = [a.to_dict() for a in episode.appearances]
        return jsonify(episode_data), 200

    
    @app.route('/episodes/<int:id>', methods=['DELETE'])
    def delete_episode(id):
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({"error": "Episode not found"}), 404

        db.session.delete(episode)
        db.session.commit()
        return '', 204

    
    @app.route('/guests', methods=['GET'])
    def get_guests():
        guests = Guest.query.all()
        return jsonify([g.to_dict() for g in guests]), 200

    
    @app.route('/appearances', methods=['POST'])
    def create_appearance():
        data = request.get_json()
        try:
            rating = int(data.get('rating'))
            episode_id = data.get('episode_id')
            guest_id = data.get('guest_id')

            
            if not (1 <= rating <= 5):
                raise ValueError("Rating must be between 1 and 5")

            
            episode = Episode.query.get(episode_id)
            guest = Guest.query.get(guest_id)

            if not episode or not guest:
                raise ValueError("Invalid episode_id or guest_id")

            
            appearance = Appearance(
                rating=rating,
                episode_id=episode_id,
                guest_id=guest_id
            )
            db.session.add(appearance)
            db.session.commit()

            return jsonify(appearance.to_dict()), 201

        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400
