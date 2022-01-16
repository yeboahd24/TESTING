import email, smtplib, ssl
from providers import PROVIDERS


def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.mailtrap.io",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'
    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"
    
    with smtplib.SMTP(
        "smtp.mailtrap.io", 2525
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)
        
        
    
def main():
    number = "+233540303211"
    message = "hello world!"
    provider = "MTN"
    
    sender_credentials = ("b66c13b8340f57", "d88a0bc8b4f9d2")
    send_sms_via_email(number, message, provider, sender_credentials)
    
    
if __name__ == "__main__":
    main()



# import smtplib

# sender = "Private Person <from@example.com>"
# receiver = "A Test User <yeboahd24@gmail.com>"

# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}

# This is a test e-mail message."""

# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#     server.login("b66c13b8340f57", "d88a0bc8b4f9d2")
#     server.sendmail(sender, receiver, message)