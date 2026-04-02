import datetime

from sqlalchemy import String, Integer, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from tickets.enums.enums import AttachmentTypeEnum
from users.model.user.orm import User

class AttachmentType(Base):
    __tablename__ = "attachment_type"

    value = Mapped[AttachmentTypeEnum] = mapped_column(Enum(AttachmentTypeEnum), nullable=False, primary_key=True)

class Attachment(Base):
    __tablename__ = "attachment"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    url = Mapped[str] = mapped_column(String(255), nullable=False)
    type = Mapped[AttachmentTypeEnum] = mapped_column(ForeignKey("attachment_type.value"), nullable=False)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

class WorkNoteAttachment(Base):
    __tablename__ = "worknote_attachments"

    worknote_id = Mapped[int] = mapped_column(ForeignKey("worknotes.id"), primary_key=True)
    attachment_id = Mapped[int] = mapped_column(ForeignKey("attachment.id"), primary_key=True)

class WorkNote(Base):
    __tablename__ = "worknotes"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    commentor = Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    note = Mapped[str] = mapped_column(Text, nullable=False)
    ticket_id = Mapped[int] = mapped_column(Integer, ForeignKey("tickets.id"), nullable=False)
    attachments = relationship("Attachment", secondary="worknote_attachments", back_populates="worknotes")