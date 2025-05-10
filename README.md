# Face Detection with OpenCV

A simple real-time face detection script using Python and OpenCV's Haar Cascade Classifier. This project uses your device's webcam to detect and highlight faces in real time.

---

## 📸 Features

- Real-time webcam capture
- Face detection using Haar cascades
- Draws bounding boxes around detected faces
- Graceful exit on key press (`a`)

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV

Install OpenCV using pip:

```bash
pip install opencv-python 

 
face_detection_project/
│
├── haarcascade_frontalface_default.xml   # Pre-trained face detection model
├── face_detect.py                        # Main script
└── README.md

RUN USING BELOW LINE
python face_detect.py

🧠 How It Works
Loads the Haar Cascade face detection model from OpenCV.

Captures video from your webcam.

Converts the video frames to grayscale for processing.

Detects faces and draws rectangles around them.

Waits for you to press "a" to exit.

