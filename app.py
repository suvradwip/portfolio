from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

services = [
    {
        "icon": "</>",
        "title": "Web Development",
        "description": "Building responsive and user-friendly websites with modern technologies."
    },
    {
        "icon": "▦",
        "title": "Data Science",
        "description": "Exploring data, finding patterns, and building useful solutions."
    },
    {
        "icon": "✦",
        "title": "Learning & Growth",
        "description": "Always curious, always learning—from BCA to beyond."
    }
]


# def get_email(email,user_message,name):
#     my_email = "robinhoodop513@gmail.com"
#     app_password = ""
#     email = request.form.get("email")
#     message = request.form.get("message")
#     msg = EmailMessage()
#     msg["Subject"] = f"Message from website {name}."
#     msg["From"] = email
#     msg["To"] = my_email
#     msg.set_content (user_message)
#     with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
#         server.login(my_email,app_password)
#         server.send_message(msg)
#     return ""



@app.route("/")
def home():
    return render_template("index.html", services=services)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    message = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        user_message = request.form.get("message", "").strip()

        if name and email and user_message:
            # Demo only: this validates the form but does not email or save it.i have update this file now it can receive the querry
            # get_email(email,user_message,name)
            message = f"Thanks, {name}! Your querry form was submitted successfully."
        else:
            message = "Please fill in all fields."
    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
