import datetime
from agents.model.agent.orm import Agent
from core.database import Base
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Skill(Base):
    __tablename__ = "skills"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = Mapped[str] = mapped_column(String(255), nullable=False)
    description = Mapped[str] = mapped_column(String(255), nullable=True)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    agents = Mapped[list["Agent"]] = relationship("Agent", secondary="agent_skills", back_populates="skills")

class AgentSkill(Base):
    __tablename__ = "agent_skills"

    agent_id = Mapped[int] = mapped_column(Integer, ForeignKey("agents.id"), primary_key=True)
    skill_id = Mapped[int] = mapped_column(Integer, ForeignKey("skills.id"), primary_key=True)

    agents = Mapped["Agent"] = relationship("Agent", back_populates="skills")
    skills = Mapped["Skill"] = relationship("Skill", back_populates="agents")