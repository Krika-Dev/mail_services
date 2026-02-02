import smtplib
import ssl

SMTP_HOST = "smtp.zoho.com"
SMTP_PORT = 465
SMTP_USER = "krika_mail@zohomail.com"
SMTP_PASS = "Krika2025**"

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context)
server.login(SMTP_USER, SMTP_PASS)

server.sendmail(
    SMTP_USER,
    SMTP_USER,
    "Subject: Prueba Zoho SMTP\n\nCorreo enviado correctamente"
)

server.quit()
print("✅ Zoho SMTP OK")
