import datetime
from sqlalchemy import ForeignKey, String, Integer, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from users.model.user.orm import Users
from backend.tickets.enums.enums import (
    TicketStatusEnum,
    TicketPriorityEnum,
    TicketSeverityEnum,
    TicketTypeEnum
)
from shared.enums import ActorTypeEnum
from tickets.model.worknotes.orm import WorkNote

class Severity(Base):
    __tablename__ = "severity"

    value = Mapped[TicketSeverityEnum] = mapped_column(Enum(TicketSeverityEnum), nullable=False, primary_key=True)

class Status(Base):
    __tablename__ = "status"

    value = Mapped[TicketStatusEnum] = mapped_column(Enum(TicketStatusEnum), nullable=False, primary_key=True)

class Priority(Base):
    __tablename__ = "priority"

    value = Mapped[TicketPriorityEnum] = mapped_column(Enum(TicketPriorityEnum), nullable=False, primary_key=True)

class Ticket(Base):
    __tablename__ = "tickets"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = Mapped[str] = mapped_column(String(255), nullable=False)
    description = Mapped[str] = mapped_column(String(255), nullable=False)
    requestor_id = Mapped[int] = mapped_column(ForeignKey("Users.id"), nullable=False)
    assignee_id = Mapped[int] = mapped_column(Integer, ForeignKey("Users.id"), nullable=True)
    type = Mapped[TicketTypeEnum] = mapped_column(Enum(TicketTypeEnum), nullable=False)
    severity = Mapped[TicketSeverityEnum] = mapped_column(ForeignKey("severity.value"), nullable=False)
    priority = Mapped[TicketPriorityEnum] = mapped_column(ForeignKey("priority.value"), nullable=False)
    status = Mapped[TicketStatusEnum] = mapped_column(ForeignKey("status.value"), nullable=False)
    worknotes_id = Mapped[list[int]] = mapped_column(ForeignKey("worknotes.id"), nullable=True)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    requestor = Mapped["Users"] = relationship("Users", back_populates="tickets")
    # assignee = Mapped["Users"] = relationship("Users", foreign_keys=[assignee_id]) #to be implemented with agents schema
    worknotes = Mapped[list["WorkNote"]] = relationship("WorkNote", back_populates="ticket")
    lock = Mapped["TicketLock"] = relationship("TicketLock", back_populates="ticket")

class TicketLock:
    __tablename__ = "ticket_lock"

    ticket_id = Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"), primary_key=True)
    actor_type = Mapped[ActorTypeEnum] = mapped_column(Enum(ActorTypeEnum), nullable=False)  # e.g., "user", "agent", "system"
    actor_id = Mapped[int] = mapped_column(Integer, nullable=False)  # ID of the user or agent who locked the ticket
    locked_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    is_leased = Mapped[bool] = mapped_column(nullable=False, default=False)  # Indicates if the lock is leased
    lease_expires_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)  # Expiration time for the lease, if applicable

    ticket = Mapped["Ticket"] = relationship("Ticket", back_populates="lock")