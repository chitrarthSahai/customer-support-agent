from typing import List, Optional

from pydantic import BaseModel, HttpUrl


class AgentCreateRequest(BaseModel):
    name: str
    url: HttpUrl
    description: Optional[str]
    prompt: str
    skills: List[int]
    tools: List[int]


class AgentUpdateRequest(BaseModel):
    name: Optional[str]
    url: Optional[HttpUrl]
    description: Optional[str]
    prompt: Optional[str]
    skills: Optional[List[int]]
    tools: Optional[List[int]]

class AgentReadResponse(BaseModel):
    id: int
    name: str
    url: HttpUrl
    description: Optional[str]
    prompt: str
    skills: List[int]
    tools: List[int]
    createdAt: str
    updatedAt: str

class AgentDeleteRequest(BaseModel):
    id: int

class AgentListResponse(BaseModel):
    total: int
    agents: List[AgentReadResponse]

class AgentExecutionCreateRequest(BaseModel):
    agentId: int
    input: str

class AgentExecutionReadResponse(BaseModel):
    id: int
    agentId: int
    input: str
    output: Optional[str]
    status: str
    createdAt: str
    updatedAt: str

class AgentExecutionListResponse(BaseModel):
    total: int
    executions: List[AgentExecutionReadResponse]

class AgentLogCreateRequest(BaseModel):
    agentId: int
    toolId: int
    payload: str

class AgentLogReadResponse(BaseModel):
    id: int
    agentId: int
    toolId: int
    payload: str
    createdAt: str

