RESPONSIVE FLASK WEBSITE
========================

1. Extract the ZIP file.
2. Open the responsive_flask_website folder in VS Code.
3. Open Terminal > New Terminal.
4. (Recommended) Create a local virtual environment:
       py -m venv .venv
       .venv\Scripts\activate
5. Install Flask:
       python -m pip install -r requirements.txt
6. Start the website:
       python app.py
7. Open this address in your browser:
       http://127.0.0.1:5000

Routes:
  /         Home
  /about    About
  /contact  Contact form

The contact form is a learning demo. It validates input and displays a confirmation,
but it does not send email or store the submitted data.

Responsive CSS notes:
  - Base rules apply to all screen sizes.
  - @media (max-width: 800px) adjusts the layout for tablets/smaller screens.
  - @media (max-width: 600px) adjusts the navigation and cards for phones.
