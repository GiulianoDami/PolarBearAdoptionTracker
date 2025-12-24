from flask import Blueprint, request, jsonify
from .models import db, Video, Annotation
from .utils import allowed_file, save_video_file

routes = Blueprint('routes', __name__)

@routes.route('/videos', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        video_path = save_video_file(file)
        video = Video(filename=file.filename, path=video_path)
        db.session.add(video)
        db.session.commit()
        return jsonify({'message': 'File successfully uploaded', 'video_id': video.id}), 201
    else:
        return jsonify({'error': 'File type not allowed'}), 400

@routes.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = Video.query.get_or_404(video_id)
    return jsonify({
        'id': video.id,
        'filename': video.filename,
        'path': video.path,
        'annotations': [{'timestamp': ann.timestamp, 'note': ann.note} for ann in video.annotations]
    })

@routes.route('/videos/<int:video_id>/annotations', methods=['POST'])
def add_annotation(video_id):
    video = Video.query.get_or_404(video_id)
    data = request.json
    annotation = Annotation(timestamp=data['timestamp'], note=data['note'], video_id=video.id)
    db.session.add(annotation)
    db.session.commit()
    return jsonify({'message': 'Annotation added successfully', 'annotation_id': annotation.id}), 201

@routes.route('/annotations/<int:annotation_id>', methods=['DELETE'])
def delete_annotation(annotation_id):
    annotation = Annotation.query.get_or_404(annotation_id)
    db.session.delete(annotation)
    db.session.commit()
    return jsonify({'message': 'Annotation deleted successfully'}), 200

@routes.route('/videos', methods=['GET'])
def list_videos():
    videos = Video.query.all()
    return jsonify([{'id': v.id, 'filename': v.filename} for v in videos])