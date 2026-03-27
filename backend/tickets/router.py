from typing import List

from fastapi import APIRouter, HTTPException

from . import service
from .schemas import TicketCreate, TicketRead

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("/", response_model=List[TicketRead])
async def list_tickets():
    return service.list_tickets()


@router.post("/", response_model=TicketRead)
async def create_ticket(payload: TicketCreate):
    return service.create_ticket(payload)


@router.get("/{ticket_id}", response_model=TicketRead)
async def get_ticket(ticket_id: int):
    t = service.get_ticket(ticket_id)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t


@router.put("/{ticket_id}", response_model=TicketRead)
async def update_ticket(ticket_id: int, payload: TicketCreate):
    t = service.update_ticket(ticket_id, payload)
    if not t:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return t


@router.delete("/{ticket_id}")
async def delete_ticket(ticket_id: int):
    ok = service.delete_ticket(ticket_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return {"status": "deleted"}
