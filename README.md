PROJECT_NAME: PolarBearAdoptionTracker

---

# Polar Bear Adoption Tracker

## Description

The **Polar Bear Adoption Tracker** is a web application designed to help researchers and wildlife conservationists monitor and track instances of polar bear adoptions. This application allows users to upload and view videos, annotate adoption events with timestamps, and share these observations with the scientific community for further analysis.

### Technologies Used
- Frontend: React.js
- Backend: Flask (Python)
- Database: SQLite
- Video Annotation: OpenCV (optional for advanced features)

## Installation

### Prerequisites
- Node.js and npm for frontend
- Python 3.8+ and pip for backend

#### Clone the repository:
bash
git clone https://github.com/techvisionary/PolarBearAdoptionTracker.git
cd PolarBearAdoptionTracker


#### Install frontend dependencies:
bash
cd frontend
npm install


#### Install backend dependencies:
bash
cd ../backend
pip install -r requirements.txt


## Usage

### Running the Frontend
Navigate to the frontend directory and start the development server:
bash
cd frontend
npm start

This will open the application in your default web browser at `http://localhost:3000`.

### Running the Backend
Ensure you are in the backend directory, then initialize the database and start the Flask server:
bash
cd ../backend
flask init-db
flask run

The backend will be accessible at `http://localhost:5000`.

### Uploading and Annotating Videos
1. From the frontend interface, upload a video of polar bears.
2. Once uploaded, you can play the video and annotate specific moments where adoption behaviors are observed.
3. Save annotations for future reference and analysis.
4. Share annotated videos with the research community through the platform.

### Viewing Shared Data
The application provides a dashboard where users can browse through annotated videos shared by other researchers, aiding in collaborative efforts to study polar bear behavior.

## Contributing

Feel free to contribute to the project by submitting pull requests or reporting issues on the [GitHub Issues page](https://github.com/techvisionary/PolarBearAdoptionTracker/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the researchers at Churchill, Manitoba, for their invaluable work and for inspiring this project.