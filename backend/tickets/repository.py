from typing import List, Optional

from .models import Ticket

_tickets: List[Ticket] = []


def list_tickets():
    return _tickets.copy()


def create_ticket(subject: str, description: str) -> Ticket:
    t = Ticket(subject=subject, description=description)
    _tickets.append(t)
    return t


def get_ticket(ticket_id: int) -> Optional[Ticket]:
    for t in _tickets:
        if t.id == ticket_id:
            return t
    return None


def update_ticket(
    ticket_id: int, subject: str, description: str
) -> Optional[Ticket]:
    t = get_ticket(ticket_id)
    if not t:
        return None
    t.subject = subject
    t.description = description
    return t


def delete_ticket(ticket_id: int) -> bool:
    global _tickets
    t = get_ticket(ticket_id)
    if not t:
        return False
    _tickets = [x for x in _tickets if x.id != ticket_id]
    return True
