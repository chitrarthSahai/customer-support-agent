from datetime import datetime
from typing import List

from pydantic import BaseModel, EmailStr
from users.enums.enums import ActionsEnums

class TicketLogCreateRequest(BaseModel):
    ticketId: int
    action: List[ActionsEnums]
    actorEmail: EmailStr


class TicketLogReadResponse(BaseModel):
    id: int
    ticketId: int
    action: List[ActionsEnums]
    actorEmail: EmailStr
    timestamp: datetime