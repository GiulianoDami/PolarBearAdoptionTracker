from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adoption_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    annotations = db.relationship('Annotation', backref='video', lazy=True)

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    print("Database initialized.")

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        new_video = Video(filename=file.filename)
        db.session.add(new_video)
        db.session.commit()
        return jsonify({'message': 'File successfully uploaded', 'video_id': new_video.id}), 201

@app.route('/annotate', methods=['POST'])
def annotate_video():
    data = request.get_json()
    video_id = data.get('video_id')
    timestamp = data.get('timestamp')
    description = data.get('description')

    if not video_id or not timestamp or not description:
        return jsonify({'error': 'Missing required fields'}), 400

    video = Video.query.get(video_id)
    if not video:
        return jsonify({'error': 'Video not found'}), 404

    new_annotation = Annotation(timestamp=timestamp, description=description, video_id=video_id)
    db.session.add(new_annotation)
    db.session.commit()
    return jsonify({'message': 'Annotation added successfully', 'annotation_id': new_annotation.id}), 201

@app.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return jsonify([{'id': video.id, 'filename': video.filename} for video in videos]), 200

@app.route('/annotations/<int:video_id>', methods=['GET'])
def get_annotations(video_id):
    annotations = Annotation.query.filter_by(video_id=video_id).all()
    return jsonify([{'id': annotation.id, 'timestamp': annotation.timestamp, 'description': annotation.description} for annotation in annotations]), 200

if __name__ == '__main__':
    app.run(debug=True)