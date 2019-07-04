from abc import ABC


class Employee(ABC):
    def __init__(self):
        self.currentCall = None
        self.rank = None

    def receive_call(self, call):
        ...

    def call_completed(self):
        ...

    def escalate_and_reassign(self):
        ...

    def assign_new_call(self):
        ...

    def is_free(self):
        return self.currentCall is None

    def get_rank(self):
        return self.rank
