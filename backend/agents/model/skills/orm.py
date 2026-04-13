import datetime
from agents.model.agent.orm import Agent
from core.database import Base
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from agents.model.tools.orm import Tools

class Skill(Base):
    __tablename__ = "skills"

    id = Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = Mapped[str] = mapped_column(String(255), nullable=False)
    description = Mapped[str] = mapped_column(String(255), nullable=True)
    instructions = Mapped[str] = mapped_column(String(255), nullable=True)
    tools = Mapped[list[int]] = mapped_column(ForeignKey("tools.id"), nullable=True)
    created_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow)
    updated_at = Mapped[DateTime] = mapped_column(DateTime, nullable=False, default_factory=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    deleted_at = Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    agents = Mapped[list["Agent"]] = relationship("Agent", secondary="agent_skills", back_populates="skills")
    tools = Mapped[list["Tools"]] = relationship("Tools", secondary="skill_tools", back_populates="skills")

class AgentSkill(Base):
    __tablename__ = "agent_skills"

    agent_id = Mapped[int] = mapped_column(Integer, ForeignKey("agents.id"), primary_key=True)
    skill_id = Mapped[int] = mapped_column(Integer, ForeignKey("skills.id"), primary_key=True)

    agents = Mapped["Agent"] = relationship("Agent", back_populates="skills")
    skills = Mapped["Skill"] = relationship("Skill", back_populates="agents")


class SkillTool(Base):
    __tablename__ = "skill_tools"

    skill_id = Mapped[int] = mapped_column(Integer, ForeignKey("skills.id"), primary_key=True)
    tool_id = Mapped[int] = mapped_column(Integer, ForeignKey("tools.id"), primary_key=True)

    skills = Mapped["Skill"] = relationship("Skill", back_populates="tools")
    tools = Mapped["Tools"] = relationship("Tools", back_populates="skills")