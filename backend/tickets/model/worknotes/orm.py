import datetime

from sqlalchemy import String, Integer, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from tickets.enums.enums import AttachmentTypeEnum
from users.model.user.orm import Users
from tickets.model.ticket.orm import Ticket

class AttachmentType(Base):
    __tablename__ = "attachment_type"

    value = Mapped[AttachmentTypeEnum] = mapped_column(Enum(AttachmentTypeEnum), nullable=False, primary_key=True)

class Attachment(Base):
    __tablename__ = "attachment"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    filename = Mapped[str] = mapped_column(String(255), nullable=False)
    url = Mapped[str] = mapped_column(String(255), nullable=False)
    type = Mapped[AttachmentTypeEnum] = mapped_column(ForeignKey("attachment_type.value"), nullable=False)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    worknotes = Mapped["WorkNote"] = relationship("worknotes", back_populates="attachments")

class WorkNote(Base):
    __tablename__ = "worknotes"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    commentor = Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    note = Mapped[str] = mapped_column(Text, nullable=False)
    ticket_id = Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"), nullable=False)
    attachment_ids = Mapped[list[int]] = mapped_column(ForeignKey("attachment.id"), nullable=True)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    attachments =  Mapped[list["Attachment"]] = relationship("Attachment", back_populates="worknotes")
    tickets = Mapped["Ticket"] = relationship("tickets", back_populates="worknotes")
    user = Mapped["Users"] = relationship("Users", back_populates="worknotes")