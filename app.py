from flask import Flask, render_template, request
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("phishing-sim")


@app.route("/", methods=["GET"])
def index():
    """
    Simulated 'Account Verification Required' phishing landing page
    for SECURETECH LAB awareness exercise. rid is a tracking id
    (e.g. passed in via query string from a GoPhish campaign link).
    """
    rid = request.args.get("rid", "")
    return render_template("login.html", rid=rid)


@app.route("/submit", methods=["POST"])
def submit():
    """
    Handles the simulated credential submission. We deliberately do
    NOT log the password — only that a submission occurred, tied to
    the tracking id, for exercise reporting purposes.
    """
    rid = request.form.get("rid", "unknown")
    email = request.form.get("email", "")
    logger.info("Simulated credential submission | rid=%s | email=%s", rid, email)
    return render_template("trained.html")


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
