from flask import Flask, render_template, request

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
            # Demo only: this validates the form but does not email or save it.
            message = f"Thanks, {name}! Your demo form was submitted successfully."
        else:
            message = "Please fill in all fields."
    return render_template("contact.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
