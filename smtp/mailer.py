from smtp.base import NotificationSender
from email.message import EmailMessage
import aiosmtplib
from core.config import settings
from models import Email

class EmailSender(NotificationSender):
	async def send(self, email: Email) -> None:

		msg = EmailMessage()

		msg['To'] = email.to
		msg['From'] = settings.smtp_config.get('username')
		msg['Subject'] = email.subject
		msg.set_content(email.body)

		await aiosmtplib.send(
            msg,
            hostname=settings.smtp_config["hostname"],
            port=settings.smtp_config["port"],
            start_tls=settings.smtp_config["start_tls"],
            username=settings.smtp_config["username"],
            password=settings.smtp_config["password"],
        )