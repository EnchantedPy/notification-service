from pydantic import BaseModel
from typing import Dict, Any

class Settings(BaseModel):
    """
    SMTP configuration for sending notifications.

    Dictionary keys:
            - hostname: Union[str, None] - The hostname of the SMTP server (e.g., 'smtp.gmail.com').
            - port: Union[int, None] - The port to connect to (e.g., 587).
            - start_tls: Union[bool, None] - Whether to use STARTTLS encryption.
            - username: Union[str, None] - SMTP username or email address.
            - password: Union[str, None] - SMTP password or app-specific password.
    """

    smtp_config: Dict[str, Any] = {
        "hostname": None,
        "port": None,
        "start_tls": None,
        "username": None,
        "password": None,
    }

settings = Settings()