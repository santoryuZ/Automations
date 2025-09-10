from bs4 import BeautifulSoup
import requests, json
from utils.emailer import send_email
from utils.logger import logger


def check_price(config):
    url = config["amazon"]["url"]
    headers = {
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/128.0.0.0 Safari/537.36"
    }

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        price_text = soup.find(name="span", class_="aok-offscreen").getText()
        price_as_float = float(price_text.replace("₹", "").replace(",", "").strip())
        title = soup.find(id="productTitle").get_text().strip()
        logger.info(f"{title} current price: ₹{price_as_float}")

        if price_as_float < config["amazon"]["target_price"]:
            message = f"{title} is on sale for {price_text}!\n{url}"
            send_email("Amazon Price Alert!", message, config)
            logger.info("Price alert sent via email!")

    except Exception as e:
        logger.error(f"Error parsing Amazon page: {e}")


if __name__ == "__main__":
    with open("../config.json") as f:
        config = json.load(f)
    check_price(config)