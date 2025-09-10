# Amazon Price Tracker 🛍️

A Python automation project that tracks the price of a product on Amazon and sends an email alert when the price drops below a desired threshold.

## Features
- Scrapes Amazon product details (title + price) using **BeautifulSoup4** and **Requests**.
- Parses and cleans price values for comparison.
- Sends **automated email alerts** with product details when price drops.
- All credentials and settings stored in **config.json** for easy configuration.
- Supports multiple products (can be extended).

## Tech Stack
- Python
- BeautifulSoup4
- Requests
- smtplib (for email)
- JSON for configuration

## Setup
1. Clone the repository:
   git clone https://github.com/yourusername/amazon-price-tracker.git
   cd amazon-price-tracker
2. 
## Install dependencies:

pip install -r requirements.txt

## Create a config.json file in the root directory:

json

{
  "email": {
    "address": "your_email@gmail.com",
    "password": "your_password",
    "smtp": "smtp.gmail.com"
  },
  "amazon": {
    "url": "https://www.amazon.in/your-product-link",
    "target_price": 3000
  }
}

## Run the tracker:

python amazon_tracker/tracker.py

## Example Alert

Subject: Amazon Price Alert!
Casio Enticer Analog Watch is on sale for ₹2,999!
https://www.amazon.in/product-link