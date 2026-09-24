from flask import Flask, render_template, request
import os
import logging

app = Flask(__name__)

# Basic logging so submissions show up in Render's log stream
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("phishing-sim")


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Simulated internal-IT credential update page for SECURETECH LAB
    phishing awareness exercise. GoPhish handles the real click/open
    tracking; this route just logs form submissions for the exercise
    report and shows the participant an "awareness" message afterward.
    """
    submitted = False
    if request.method == "POST":
        username = request.form.get("username", "")
        # NOTE: For the training exercise, do NOT log real passwords.
        # We only log that a submission happened + the username field,
        # to avoid storing sensitive data even in a simulated context.
        logger.info("Simulated credential submission from username field: %s", username)
        submitted = True

    return render_template("index.html", submitted=submitted)


@app.route("/health")
def health():
    # Simple health check endpoint for Render
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
