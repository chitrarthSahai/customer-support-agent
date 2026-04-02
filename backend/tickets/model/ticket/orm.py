from sqlalchemy import String, Integer, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from backend.tickets.enums.enums import (
    TicketStatusEnum,
    TicketPriorityEnum,
    TicketSeverityEnum,
    TicketTypeEnum
)

class Severity(Base):
    __tablename__ = "severity"

    value = Mapped[TicketSeverityEnum] = mapped_column(Enum(TicketSeverityEnum), nullable=False, primary_key=True)

class Status(Base):
    __tablename__ = "status"

    value = Mapped[TicketStatusEnum] = mapped_column(Enum(TicketStatusEnum), nullable=False, primary_key=True)

class Priority(Base):
    __tablename__ = "priority"

    value = Mapped[TicketPriorityEnum] = mapped_column(Enum(TicketPriorityEnum), nullable=False, primary_key=True)

