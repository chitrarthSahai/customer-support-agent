from enum import Enum

class ActorTypeEnum(str, Enum):
    USER = "user"
    AGENT = "agent"
    SYSTEM = "system"