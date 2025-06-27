from typing import Protocol
from models import Email


class NotificationSender(Protocol):

	async def send(self, *args, **kwargs) -> None:
		...