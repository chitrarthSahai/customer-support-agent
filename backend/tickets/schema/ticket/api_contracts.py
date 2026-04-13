from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr
from tickets.enums.enums import (
    TicketStatusEnum,
    TicketPriorityEnum,
    TicketSeverityEnum,
    TicketTypeEnum
)


class TicketCreateRequest(BaseModel):
    title: str
    description: str
    requestorEmail: EmailStr
    priority: Optional[TicketPriorityEnum] = TicketPriorityEnum.MEDIUM


class TicketUpdateRequest(BaseModel):
    title: Optional[str]
    description: Optional[str]
    assigneeEmail: Optional[EmailStr]
    priority: Optional[TicketPriorityEnum]
    status: Optional[TicketStatusEnum]
    type: Optional[TicketTypeEnum]
    severity: Optional[TicketSeverityEnum]

class TicketDeleteRequest(BaseModel):
    id: int

class TicketReadResponse(BaseModel):
    id: int
    title: str
    description: str
    requestorEmail: EmailStr
    assigneeEmail: Optional[EmailStr]
    priority: TicketPriorityEnum
    status: TicketStatusEnum
    type: TicketTypeEnum
    severity: TicketSeverityEnum
    createdAt: datetime
    updatedAt: datetime


class TicketListResponse(BaseModel):
    total: int
    tickets: List[TicketReadResponse]