from .Webhook import Webhook
from .core import validate_payload
webhook = Webhook()

__all__ = ["webhook", "validate_payload"]