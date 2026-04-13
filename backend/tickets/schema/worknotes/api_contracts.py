from datetime import datetime
from typing import List

from pydantic import BaseModel, EmailStr, HttpUrl
from tickets.enums.enums import AttachmentTypeEnum

class AttachmentCreateRequest(BaseModel):
    filename: str
    filetype: AttachmentTypeEnum
    url: HttpUrl

class AttachmentUpdateRequest(BaseModel):
    filename: str
    filetype: AttachmentTypeEnum
    url: HttpUrl

class AttachmentReadResponse(BaseModel):
    id: int
    filename: str
    filetype: AttachmentTypeEnum
    url: HttpUrl
    createdAt: datetime
    updatedAt: datetime

class AttachmentDeleteRequest(BaseModel):
    id: int

class AttachmentListResponse(BaseModel):
    total: int
    attachments: List[AttachmentReadResponse]



class WorkNoteCreateRequest(BaseModel):
    commentorEmail: EmailStr
    note: str
    ticketId: int
    attachments: List[AttachmentCreateRequest] = []

class WorkNoteUpdateRequest(BaseModel):
    commentorEmail: EmailStr
    note: str
    ticketId: int
    attachments: List[AttachmentUpdateRequest] = []

class WorkNoteReadResponse(BaseModel):
    id: int
    commentorEmail: EmailStr
    note: str
    ticketId: int
    attachments: List[AttachmentReadResponse] = []
    createdAt: datetime
    updatedAt: datetime

class WorkNoteDeleteRequest(BaseModel):
    id: int

class WorkNoteListResponse(BaseModel):
    total: int
    worknotes: List[WorkNoteReadResponse]