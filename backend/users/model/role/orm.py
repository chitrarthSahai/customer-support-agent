from core.database import Base
from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from users.enums.enums import ActionsEnums, RoleEnum


class Role(Base):
    __tablename__ = "Roles"

    name = Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), primary_key=True)
    description = Mapped[str] = mapped_column(String(255), nullable=False)


class Actions(Base):
    __tablename__ = "Actions"

    scope = Mapped[ActionsEnums] = mapped_column(
        Enum(ActionsEnums), primary_key=True
    )


class RoleActions(Base):
    __tablename__ = "RoleActions"

    role = Mapped[RoleEnum] = mapped_column(
        Enum(RoleEnum), ForeignKey("Roles.name"), primary_key=True
    )
    action = Mapped[ActionsEnums] = mapped_column(
        Enum(ActionsEnums), ForeignKey("Actions.scope"), primary_key=True
    )
