from typing import List, Optional

from pydantic import BaseModel


class SkillCreateRequest(BaseModel):
    name: str
    instructions: str
    resources: Optional[str]
    tools: Optional[List[int]]
    description: Optional[str]

class SkillUpdateRequest(BaseModel):
    name: Optional[str]
    instructions: Optional[str]
    resources: Optional[str]
    tools: Optional[List[int]]
    description: Optional[str]


class SkillReadResponse(BaseModel):
    id: int
    name: str
    instructions: str
    resources: Optional[str]
    tools: Optional[List[int]]
    description: Optional[str]
    createdAt: str
    updatedAt: str

class SkillDeleteRequest(BaseModel):
    id: int


class SkillListResponse(BaseModel):
    total: int
    skills: List[SkillReadResponse]

