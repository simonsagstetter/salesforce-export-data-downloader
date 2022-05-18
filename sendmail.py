# COPYRIGHT @ 2022 Simon, Sagstetter
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(CONFIG):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Salesforce Backup Job Successfull"
    message["From"] = CONFIG.SENDER
    message["To"] = CONFIG.RECEIVER

    text = """\
    Salesforce Export Data Link has been downloaded.
    """
    html = """\
    <html>
      <body>
        <p>
           Salesforce Export Data Link has been downloaded.
        </p>
      </body>
    </html>
    """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    with smtplib.SMTP("localhost") as server:
        server.sendmail(
            CONFIG.sender, CONFIG.receiver, message.as_string()
        )
