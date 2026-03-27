from typing import List

from . import repository
from .schemas import TicketCreate, TicketRead


def list_tickets() -> List[TicketRead]:
    tickets = repository.list_tickets()
    return [
        TicketRead(id=t.id, subject=t.subject, description=t.description)
        for t in tickets
    ]


def create_ticket(data: TicketCreate) -> TicketRead:
    t = repository.create_ticket(
        subject=data.subject, description=data.description
    )
    return TicketRead(id=t.id, subject=t.subject, description=t.description)


def get_ticket(ticket_id: int) -> TicketRead | None:
    t = repository.get_ticket(ticket_id)
    if not t:
        return None
    return TicketRead(id=t.id, subject=t.subject, description=t.description)


def update_ticket(ticket_id: int, data: TicketCreate) -> TicketRead | None:
    t = repository.update_ticket(
        ticket_id, subject=data.subject, description=data.description
    )
    if not t:
        return None
    return TicketRead(id=t.id, subject=t.subject, description=t.description)


def delete_ticket(ticket_id: int) -> bool:
    return repository.delete_ticket(ticket_id)
