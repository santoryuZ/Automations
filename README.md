## Final Repo Structure
automation-suite/
│── README.md              # Root README (covers both projects)
│── requirements.txt       # Dependencies
│── config.json            # Credentials + settings
│
├── amazon_tracker/
│   ├── tracker.py
│   └── README.md
│
├── web_form_automation/
│   ├── form_bot.py
│   └── README.md
│
└── utils/
    ├── emailer.py
    ├── logger.py
    └── __init__.py

📄 Root README.md
# Automation Suite 🚀

A modular automation suite built with **Python, Selenium, and BeautifulSoup**.  
It demonstrates two real-world automation workflows:

- 🛒 **Amazon Price Tracker** → Scrapes product prices and sends email alerts if they fall below a threshold.
- 💼 **Job Portal Easy Apply Automation** → Automates login, navigation, form filling, and submission workflows on a job portal.

---

## Features
- Web scraping with **BeautifulSoup4** + Requests
- Browser automation with **Selenium WebDriver**
- Automated email notifications via **SMTP**
- Config-driven design (`config.json`)
- Logging and error handling for robustness
- Modular structure for extensibility

---

## Tech Stack
- Python 3.x
- Selenium WebDriver
- BeautifulSoup4
- Requests
- SMTP (email alerts)
- JSON (configuration)

---

## Setup
1. Clone the repository:
   git clone https://github.com/yourusername/automation-suite.git
   cd automation-suite


## Install dependencies:

pip install -r requirements.txt


Update config.json with your email credentials, product URL, target price, and job portal credentials.

## Usage
Run Amazon Price Tracker
python amazon_tracker/tracker.py

Run Job Portal Automation
python web_form_automation/form_bot.py

## Why This Project?

This suite showcases:
End-to-end automation workflows
Test automation concepts (dynamic waits, form submission, navigation)
Reusable utilities (logging + email notifications)
Config-driven design (no hardcoding of sensitive data)
