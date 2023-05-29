import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import getpass
import os

class Finish:
    def __init__(self, synthetic_dataset, scorecard_results):
        self.synthetic_dataset = synthetic_dataset
        self.scorecard_results = scorecard_results

    def generate_csv(self, filename):
        self.synthetic_dataset.to_csv(filename, index=False)
        print(f"Synthetic dataset saved as {filename}")

    def send_email(self, sender_email, receiver_email, subject, body, attachment_path):
        # Create a multipart message and set the email headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Add the body to the email
        message.attach(MIMEText(body, "plain"))

        # Open the attachment file and add it to the email
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode the attachment and add a header
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(attachment_path)}",
        )

        # Add the attachment to the email message
        message.attach(part)

        # Convert the message to a string and send the email
        text = message.as_string()

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Prompt the user for their email password
        password = getpass.getpass("Enter your email password: ")

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")
        except Exception as e:
            print("An error occurred while sending the email:", str(e))