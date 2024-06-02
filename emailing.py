import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "elmuevdszcbyxvhi"
SENDER = "niewadzilukasz@gmail.com"
RECEIVER = "niewadzilukasz@gmail.com"

def send_email(file_patch):
    print("before sending email")
    email_message = EmailMessage()
    email_message["Subiect"] = "Movement Detected!"
    email_message.set_content("Someone is at your doorstep!")

    with open(file_patch, "rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("after sending email")
