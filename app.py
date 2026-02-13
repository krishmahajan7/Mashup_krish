from mashup_logic import create_mashup
from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
import re
import zipfile

app = Flask(__name__)

# ---------------- Email Configuration ----------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'krishmahajan555@gmail.com'   # Replace
app.config['MAIL_PASSWORD'] = 'fvaa befu okik vcew'      # Replace

mail = Mail(app)


# ---------------- Email Validation ----------------
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)
# ---------------- Routes ----------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    singer = request.form.get("singer")
    num_videos = request.form.get("num_videos")
    duration = request.form.get("duration")
    email = request.form.get("email")

    # Validation
    if not singer or not num_videos or not duration or not email:
        return "All fields are required!"

    if not is_valid_email(email):
        return "Invalid Email Address!"

    try:
        num_videos = int(num_videos)
        duration = int(duration)

        if num_videos <= 10:
            return "Number of videos must be greater than 10."

        if duration <= 20:
            return "Duration must be greater than 20 seconds."

        # Create mashup
        create_mashup(singer, num_videos, duration)

        # Send Email
        msg = Message(
            subject="Your Mashup File",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )

        msg.body = "Your mashup file is attached."
        msg.attach("mashup.zip", "application/zip", open("mashup.zip", "rb").read())

        mail.send(msg)

        return "Success! Mashup sent to your email."

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
