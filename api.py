from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models import Email
from smtp.mailer import EmailSender
from contextlib import asynccontextmanager
from aiosmtplib.errors import SMTPException

@asynccontextmanager
async def lifespan(app: FastAPI):
	app.state.email_sender = EmailSender()
	yield
	app.state.email_sender = None

app = FastAPI(lifespan=lifespan)

@app.exception_handler(SMTPException)
async def value_error_handler(request: Request, exc: SMTPException):
    return JSONResponse(
        status_code=400,
        content={"detail": f"Error sending email: {str(exc)}"},
    )

"""
Notifications API

This microservice provides endpoints for sending emails and checking the health status of the service.
"""

@app.get('/healthcheck')
async def healthcheck():
    """
    Healthcheck endpoint to verify the service is running.
    """
    return {'status': 'healthy'}

@app.post('/send/email')
async def send_email(email: Email, request: Request):
    """
    Endpoint to send an email.

    Args:
        email (Email): The email object containing recipient, subject, and body.
        request (Request): The request object.

    Returns:
        dict: A success status message.
    """
    sender = request.app.state.email_sender
    await sender.send(email)
    return {'status': 'success'}