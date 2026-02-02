from fastapi import FastAPI, HTTPException, Header
from app.schemas import MailRequest
from app.mailer import send_mail
from app.config import API_KEY

app = FastAPI(title="Mailer Service")

@app.post("/send")
def send_email(
    payload: MailRequest,
    x_api_key: str = Header(...)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    send_mail(payload)
    return {"status": "ok"}
