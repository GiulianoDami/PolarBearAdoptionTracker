from flask import Blueprint, request, jsonify
from .models import db, Video, Annotation
from .utils import save_video_file

routes = Blueprint('routes', __name__)

@routes.route('/videos', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400
    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    video_path = save_video_file(video_file)
    new_video = Video(filename=video_file.filename, path=video_path)
    db.session.add(new_video)
    db.session.commit()
    return jsonify({'message': 'Video uploaded successfully', 'video_id': new_video.id}), 201

@routes.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = Video.query.get_or_404(video_id)
    return jsonify({
        'id': video.id,
        'filename': video.filename,
        'path': video.path,
        'annotations': [{'timestamp': annotation.timestamp, 'description': annotation.description} for annotation in video.annotations]
    })

@routes.route('/videos/<int:video_id>/annotations', methods=['POST'])
def add_annotation(video_id):
    video = Video.query.get_or_404(video_id)
    data = request.json
    timestamp = data.get('timestamp')
    description = data.get('description')
    if not timestamp or not description:
        return jsonify({'error': 'Timestamp and description are required'}), 400
    new_annotation = Annotation(timestamp=timestamp, description=description, video_id=video.id)
    db.session.add(new_annotation)
    db.session.commit()
    return jsonify({'message': 'Annotation added successfully', 'annotation_id': new_annotation.id}), 201

@routes.route('/annotations', methods=['GET'])
def get_all_annotations():
    annotations = Annotation.query.all()
    return jsonify([{'id': annotation.id, 'timestamp': annotation.timestamp, 'description': annotation.description, 'video_id': annotation.video_id} for annotation in annotations])