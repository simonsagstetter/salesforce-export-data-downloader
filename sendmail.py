# COPYRIGHT @ 2022 Simon, Sagstetter
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(CONFIG):
    smtp_host = CONFIG.SMTP_HOST
    smtp_port = CONFIG.SMTP_PORT
    smtp_user = CONFIG.SMTP_USER
    smtp_password = CONFIG.SMTP_PASSWORD

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
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(
            CONFIG.SENDER, CONFIG.RECEIVER, message.as_string()
        )
