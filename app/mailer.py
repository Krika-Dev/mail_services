import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from app.config import *

env = Environment(
    loader=FileSystemLoader("app/templates")
)

def send_mail(payload):
    template = env.get_template(payload.template)
    html = template.render(**payload.variables)

    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(
        SMTP_HOST,
        SMTP_PORT,
        context=context,
        timeout=30
    )

    server.login(SMTP_USER, SMTP_PASS)

    for email in payload.to:
        # 🔑 CREAR MENSAJE NUEVO POR CADA DESTINATARIO
        msg = MIMEMultipart("alternative")
        msg["From"] = MAIL_FROM
        msg["To"] = email
        msg["Subject"] = payload.subject

        msg.attach(MIMEText(html, "html"))

        server.sendmail(MAIL_FROM, email, msg.as_string())

    server.quit()
