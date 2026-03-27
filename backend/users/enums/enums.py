from enum import Enum


class UserStatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class RoleEnum(str, Enum):
    ADMIN = "admin"
    AGENT = "agent"
    CUSTOMER = "customer"


class ActionsEnums(str, Enum):
    USERCREATE = "user.create"
    USERREAD = "user.read"
    USERUPDATE = "user.update"
    USERDELETE = "user.delete"
    ROLECREATE = "role.create"
    ROLEREAD = "role.read"
    ROLEUPDATE = "role.update"
    ROLEDELETE = "role.delete"
    TICKETCREATE = "ticket.create"
    TICKETREAD = "ticket.read"
    TICKETUPDATE = "ticket.update"
    COMMENTCREATE = "comment.create"
    COMMENTREAD = "comment.read"
    COMMENTUPDATE = "comment.update"
    COMMENTDELETE = "comment.delete"
    ATTACHMENTCREATE = "attachment.create"
    ATTACHMENTREAD = "attachment.read"
    ATTACHMENTDELETE = "attachment.delete"
    AGENTCREATE = "agent.create"
    AGENTREAD = "agent.read"
    AGENTUPDATE = "agent.update"
    AGENTDELETE = "agent.delete"
    TOOLCREATE = "tool.create"
    TOOLREAD = "tool.read"
    TOOLUPDATE = "tool.update"
    TOOLDELETE = "tool.delete"
    SKILLSCREATE = "skills.create"
    SKILLSREAD = "skills.read"
    SKILLSUPDATE = "skills.update"
    SKILLSDELETE = "skills.delete"
