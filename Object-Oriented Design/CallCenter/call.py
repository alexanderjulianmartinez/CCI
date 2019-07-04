class Call:
    def __init__(self, caller):
        self.rank = None
        self.handler = None
        self.caller = caller

    def set_handler(self, employee):
        self.handler = employee

    def reply(self, message):
        print(message)

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def increment_rank(self):
        self.rank += 1

    def disconnect(self):
        self.caller = None
