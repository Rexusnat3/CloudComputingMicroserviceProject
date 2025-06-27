from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from app.email_sender import send_email

app = FastAPI()

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str

@app.post("/send-email")
def send_email_endpoint(email: EmailRequest):
    success = send_email(email.to, email.subject, email.body)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to send email")
    return {"message": "Email sent successfully"}
