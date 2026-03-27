import datetime

from core.database import Base
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from users.enums.enums import UserStatusEnum


class Users(Base):
    __tablename__ = "Users"

    id = Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name = Mapped[str] = mapped_column(String(255), nullable=False)
    email = Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False
    )
    role = Mapped["Role"] = mapped_column(
        ForeignKey("Roles.name"), nullable=False
    )
    title = Mapped[str] = mapped_column(String(255), nullable=True)
    last_login = Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    is_active = Mapped["UserStatus"] = mapped_column(
        ForeignKey("UserStatus.status"), nullable=False
    )
    created_at = Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, default_factory=datetime.utcnow
    )
    updated_at = Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        default_factory=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    tickets = Mapped[list["Ticket"]] = relationship(back_populates="user")
    worknotes = Mapped[list["WorkNote"]] = relationship(back_populates="user")


class UserStatus(Base):
    __tablename__ = "UserStatus"

    status: Mapped[UserStatusEnum] = mapped_column(
        Enum(UserStatusEnum), primary_key=True
    )
