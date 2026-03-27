from pydantic import BaseModel


class TicketCreate(BaseModel):
    subject: str
    description: str


class TicketRead(BaseModel):
    id: int
    subject: str
    description: str

    class Config:
        orm_mode = True
