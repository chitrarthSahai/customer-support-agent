import datetime
from agents.model.skills.orm import Skill
from agents.model.tools.orm import Tools
from core.database import Base
from sqlalchemy import DateTime, Integer, String, Text, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Agent(Base):
    __tablename__ = "agents"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = Mapped[str] = mapped_column(String(255), nullable=False)
    url = Mapped[str] = mapped_column(String(255), nullable=True)
    prompt = Mapped[str] = mapped_column(Text, nullable=True)
    skill_ids = Mapped[list[int]] = mapped_column(ForeignKey("skills.id"), nullable=True)
    description = Mapped[str] = mapped_column(String(255), nullable=True)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    skills = Mapped[list["Skill"]] = relationship("Skill", secondary="agent_skills", back_populates="agents")
    tools = Mapped[list["Tools"]] = relationship("Tools", secondary="agent_tools", back_populates="agents")


class AgentLog(Base):
    __tablename__ = "agent_logs"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    agent_id = Mapped[int] = mapped_column(Integer, ForeignKey("agents.id"), nullable=False)
    tool_id = Mapped[int] = mapped_column(Integer, ForeignKey("tools.id"), nullable=True)
    payload = Mapped[dict] = mapped_column(JSON, nullable=True)