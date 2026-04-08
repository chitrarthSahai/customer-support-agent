import datetime

from agents.model.agent.orm import Agent
from core.database import Base
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from agents.enums.enums import ToolTypeEnum


class Tools(Base):
    __tablename__ = "tools"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = Mapped[str] = mapped_column(String(255), nullable=False)
    description = Mapped[str] = mapped_column(Text, nullable=True)
    tool_type = Mapped[ToolTypeEnum] = mapped_column(Enum(ToolTypeEnum), nullable=False)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    agents = Mapped[list["Agent"]] = relationship("Agent", secondary="agent_tools", back_populates="tools")


class AgentTool(Base):
    __tablename__ = "agent_tools"

    agent_id = Mapped[int] = mapped_column(Integer, ForeignKey("agents.id"), primary_key=True)
    tool_id = Mapped[int] = mapped_column(Integer, ForeignKey("tools.id"), primary_key=True)

    agents = Mapped["Agent"] = relationship("Agent", back_populates="tools")
    tools = Mapped["Tools"] = relationship("Tools", back_populates="agents")