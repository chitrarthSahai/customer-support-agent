from enum import Enum


class ToolType(str, Enum):
    LOCAL = "local"
    HTTP = "http"
    SSE = "sse"