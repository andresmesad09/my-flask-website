from flask import Flask, redirect, request, flash
from flask import render_template
import requests
import time
import json
import base64
import html

app = Flask(__name__)
LAMBDA_URL = "https://drnvcqxvjujshgpzco7375j3ui0gdlgp.lambda-url.us-east-1.on.aws/"


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/contact", methods=["POST"])
def contact_me():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")
    body = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message
    }
    response = requests.post(url=LAMBDA_URL, json=body)
    response.raise_for_status()
    response_object = response.json()
    print(response.status_code)
    body = response_object['event']['body']
    print(body)
    time.sleep(2)
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True)
