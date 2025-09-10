Job Portal Easy Apply Automation – README.md
# Job Portal Easy Apply Automation 💼

A Python automation project that uses **Selenium WebDriver** to streamline the process of applying to jobs on a job portal.  
The bot automates login, navigates to job postings, clicks **Easy Apply**, fills out application forms, and submits applications — simulating a real user workflow.

## Features
- Automates login with stored credentials.
- Navigates directly to job postings via URL.
- Clicks **Easy Apply** buttons on job listings.
- Fills text fields, radio buttons, and checkboxes in the application form.
- Reviews and submits applications automatically.
- Uses **explicit waits** for dynamic elements.
- Includes **error handling** for missing elements and timeouts.
- Stores credentials and target job URLs in `config.json`.

## Tech Stack
- Python
- Selenium WebDriver
- ChromeDriver
- JSON for configuration

## Setup
1. Clone the repository:
   git clone https://github.com/yourusername/job-portal-automation.git
   cd job-portal-automation


## Install dependencies:

pip install -r requirements.txt


## Create a config.json file in the root directory:

{
  "job_portal": {
    "username": "your_email@example.com",
    "password": "your_password",
    "job_url": "https://example.com/jobs/view/12345"
  }
}


## Run the automation:

python web_form_automation/form_bot.py

## Example Workflow:

Script logs into the job portal.

Navigates to the specified job posting.

Clicks Easy Apply.

Fills out required fields (e.g., short answers, availability).

Reviews and submits the application.