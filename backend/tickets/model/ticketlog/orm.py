import datetime

from sqlalchemy import ForeignKey, String, Integer, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from users.model.user.orm import Users
from tickets.model.ticket.orm import Ticket


class TicketLog(Base):
    __tablename__ = "ticket_log"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ticket_id = Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"), nullable=False)
    action = Mapped[str] = mapped_column(String(255), nullable=False)
    actor_id = Mapped[int] = mapped_column(Integer, ForeignKey("Users.id"), nullable=False)
    timestamp = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)

    actor = Mapped["Users"] = relationship("Users", back_populates="ticket_logs")
    ticket = Mapped["Ticket"] = relationship("Ticket", back_populates="logs")