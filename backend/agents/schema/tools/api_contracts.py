from typing import List, Optional

from pydantic import BaseModel, model_validator

from agents.enums.enums import ToolType


class ToolCreateRequest(BaseModel):
    name: str
    description: Optional[str]
    toolType: ToolType
    command: Optional[str]
    args: Optional[str]
    url: Optional[str]
    headers: Optional[dict]

    @model_validator(mode="after")
    def validate_tool(self):
        if self.toolType == ToolType.LOCAL and not self.command:
            raise ValueError("Command is required for local tool type")
        if self.toolType in [ToolType.HTTP, ToolType.SSE] and not self.url:
            raise ValueError("URL is required for http and sse tool types")
        return self

class ToolUpdateRequest(BaseModel):
    name: Optional[str]
    description: Optional[str]
    toolType: Optional[ToolType]
    command: Optional[str]
    args: Optional[str]
    url: Optional[str]
    headers: Optional[dict]

    @model_validator(mode="after")
    def validate_tool(self):
        if self.toolType == ToolType.LOCAL and not self.command:
            raise ValueError("Command is required for local tool type")
        if self.toolType in [ToolType.HTTP, ToolType.SSE] and not self.url:
            raise ValueError("URL is required for http and sse tool types")
        return self
    

class ToolReadResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    toolType: ToolType
    command: Optional[str]
    args: Optional[str]
    url: Optional[str]
    headers: Optional[dict]
    createdAt: str
    updatedAt: str

class ToolDeleteRequest(BaseModel):
    id: int