# Phishing Landing Page — SecureTech Lab

A Flask-based phishing simulation landing page built for internal security awareness training as part of the **SecureTech Lab** project. This app is deployed on [Render](https://render.com) and integrates with a [GoPhish](https://getgophish.com) campaign for click tracking.

> ⚠️ **For authorized security awareness training only.** This project simulates a phishing login page to help organizations educate employees about phishing threats. It must only be used with proper authorization from the organization running the exercise.

## 🧩 How It Works

1. GoPhish sends a tracking link (`track.phishguard.world/?rid=XXXX`) in a simulated phishing email.
2. When the link is clicked, GoPhish logs the **"Clicked Link"** event and redirects the user to this Flask app.
3. The Flask app displays a fake **"Account Verification Required"** login page.
4. If the user submits the form, no real credentials are stored — only the fact that a submission occurred is logged, for reporting purposes.
5. The user is then shown an **awareness page** explaining that this was a simulated phishing exercise, along with tips on spotting real phishing attempts.

## 🏗️ Tech Stack

- **Backend:** Flask (Python)
- **WSGI Server:** Gunicorn
- **Hosting:** Render.com
- **Campaign Tracking:** GoPhish
- **Domain / DNS:** Namecheap (custom subdomain routing)

## 📁 Project Structure
