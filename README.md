#🎵Singer Mashup Generator

##Project Overview

Mashup Video Generator is a Flask-based web service that allows users to generate a custom mashup of their favorite singer's songs.

Users provide:
- Singer Name
- Number of Videos
- Duration of Each Video (in seconds)
- Email Address

The system automatically:
1. Scrapes videos from YouTube
2. Extracts and clips media
3. Merges clips into a mashup
4. Compresses the result into a `.zip` file
5. Sends the final file to the user via email

This project demonstrates backend processing, media handling, web integration, and automated email delivery.

---

#Features

- Automated Video Scraping using yt-dlp
- Dynamic Clipping of audio/video
- Automatic Mashup Generation
- ZIP File Creation
- Email Delivery System
- Flask-based Web Interface
- Input Validation (Video count, duration, email format)
- Temporary File Cleanup after processing

---

#Tech Stack

## Backend
- Python
- Flask
- yt-dlp
- MoviePy / FFmpeg
- smtplib
- zipfile

## Frontend
- HTML
- CSS

## Media Processing
- FFmpeg

---

#Prerequisites

Before running this project, ensure the following are installed:

- Python 3.9+
- pip
- FFmpeg (must be installed and added to system PATH)

---


#Installation Guide

## Clone the Repository

```bash
git clone https://github.com/your-username/mashup-video-generator.git
cd mashup-video-generator
```

##Create Virtual Environment (Recommended)

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

##Install Dependencies

```bash
pip install -r requirements.txt
```

---

#requirements.txt

```
Flask
yt-dlp
moviepy
pydub
python-dotenv
requests
email-validator
```

---

#Environment Variables Setup (Email Configuration)

Create a `.env` file in the root directory:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```
---

#Running the Application

Start the Flask server:

```bash
python app.py
```

Open browser and visit:

```
http://127.0.0.1:5000/
```
----
#System Architecture

##Frontend Layer
- HTML form collects user input.
- Sends POST request to Flask backend.

##Flask Backend
- Validates input data.
- Calls mashup processing functions.
- Handles file compression and email delivery.

##Processing Layer
- yt-dlp → Downloads videos
- FFmpeg → Converts media formats
- MoviePy / pydub → Clips and merges media
- zipfile → Compresses final output

##Email Service Layer
- smtplib sends ZIP file to user’s email.

---

# 📂 Project Structure

```
mashup-video-generator/
│
├── app.py
├── mashup.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── README.md
```

---

# Output

User receives:

mashup_result.zip

Inside ZIP:
mashup.mp3 (or mashup.mp4)

---

#Input Validation Rules

- Number of videos must be greater than 10
- Duration must be greater than 20 seconds
- Email must be valid format
- Output sent only after successful processing

----

#License

This project is developed for educational purposes.

---

#Author

Krish Mahajan  
