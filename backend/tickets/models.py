class Ticket:
    _id_seq = 1

    def __init__(self, subject: str, description: str):
        self.id = Ticket._id_seq
        Ticket._id_seq += 1
        self.subject = subject
        self.description = description
