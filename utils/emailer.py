import smtplib
import json

def send_email(subject, message, config):
    email_config = config["email"]
    with smtplib.SMTP(email_config["smtp"], port=587) as connection:
        connection.starttls()
        connection.login(email_config["address"], email_config["password"])
        connection.sendmail(
            from_addr=email_config["address"],
            to_addrs=email_config["address"],
            msg=f"Subject:{subject}\n\n{message}".encode("utf-8")
        )