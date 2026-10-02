<div align="center">

# 🎣 Phishing Simulation Landing Page

### SecureTech Lab — Security Awareness Training Platform

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-black.svg)](https://flask.palletsprojects.com/)
[![Deployed on Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7.svg)](https://render.com)
[![License](https://img.shields.io/badge/License-Internal%20Use-lightgrey.svg)](#license)

A Flask-based phishing simulation landing page built for internal security awareness training. Deployed on Render.com and integrated with a GoPhish campaign for click tracking and reporting.

</div>

---

## ⚠️ Disclaimer

> This project is built **exclusively for authorized, internal security awareness training**. It simulates a phishing login page to help organizations educate employees about social engineering threats. It must only be deployed and used with explicit authorization from the organization conducting the exercise. Unauthorized use to collect credentials from individuals without consent is illegal and unethical.
---


## 🔍 Overview

This application serves as the **credential-capture simulation layer** of a larger phishing awareness exercise. GoPhish handles campaign management and click tracking, while this Flask app renders the actual fake login experience and the post-submission awareness message.

**Flow summary:**


---

## 🏗️ Architecture

| Component | Technology | Role |
|---|---|---|
| Campaign management & tracking | GoPhish | Sends simulated phishing emails, tracks clicks |
| Landing page / credential capture | Flask (this repo) | Renders fake login page, logs submissions |
| Hosting | Render.com | Hosts the Flask app as a web service |
| DNS / Domain | Namecheap | Routes `sim.phishguard.world` to Render |
| SSL/TLS | Render (Let's Encrypt) | Auto-issued certificate for HTTPS |


## 📁 Project Structure


## ⚙️ Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/Nigar-Mustafayeva/phishing-landing.git
cd phishing-landing

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app locally
python app.py
```

The app will be available at **http://localhost:5000**.

---

## ☁️ Deployment

This app is deployed on **Render.com** as a Web Service.

| Setting | Value |
|---|---|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Runtime | Python 3.14 |
| Auto-Deploy | Enabled on push to `main` |

---

## 🌐 Domain & DNS Configuration

The app is served on a custom subdomain:

**DNS setup (Namecheap → Advanced DNS):**

| Type | Host | Value |
|---|---|---|
| CNAME | `sim` | `phishing-landing-1.onrender.com` |

Once verified on Render, SSL is automatically issued via Let's Encrypt — no manual certificate management required.

---

## 🎣 GoPhish Integration

GoPhish is configured with a lightweight redirect landing page that:

1. Logs the **"Clicked Link"** event when a recipient opens the tracking link.
2. Immediately redirects to `https://sim.phishguard.world/?rid={{.RId}}`, preserving the tracking ID.
3. Leaves `Capture Submitted Data` and `Capture Passwords` **disabled** in GoPhish — this Flask app is the single source of truth for submission logging.

---

## 🔒 Security & Privacy

- ❌ **Real passwords are never logged or stored**, under any circumstance.
- ✅ Only the fact that a submission occurred — along with the tracking ID (`rid`) and the email field — is logged, strictly for exercise reporting.
- ✅ Intended **only** for authorized, internal security awareness exercises with proper organizational sign-off.
- ⚠️ Deploying this outside of an authorized training context may violate computer fraud and data protection laws.

---

## 🗺️ Roadmap

- [ ] Webhook integration between Flask and GoPhish for unified "Submitted Data" reporting
- [ ] Automated post-campaign report generation
- [ ] Support for multiple landing page templates per campaign
- [ ] Rate limiting / abuse protection on `/submit`

---

