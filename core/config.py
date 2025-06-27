from pydantic import BaseModel
from typing import Dict, Any

class Settings(BaseModel):
	smtp_config: Dict[str, Any] = {
    "hostname": "...",
    "port": 587,
    "start_tls": True,
    "username": "...",
    "password": "...",
	 }

settings = Settings()