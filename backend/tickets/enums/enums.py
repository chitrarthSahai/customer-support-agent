from enum import Enum


class TicketStatusEnum(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class TicketPriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class TicketSeverityEnum(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


class TicketTypeEnum(str, Enum):
    REQUEST = "request"
    INCIDENT = "incident"
    SUPPORT = "support"


class AttachmentTypeEnum(str, Enum):
    IMAGE = "image"
    DOCUMENT = "document"
    VIDEO = "video"
    OTHER = "other"
