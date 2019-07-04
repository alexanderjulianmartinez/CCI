class CallHandler:
    def __init__(self, num_respondents, num_managers, num_directors):
        self.levels = 3
        self.callQueues = []
        self.employeeLevels = [None]*self.levels
        self.employeeLevels[0] = [None]*num_respondents
        self.employeeLevels[1] = [None]*num_managers
        self.employeeLevels[2] = [None]*num_directors

    def get_handler_for_call(self, call):
        ...

    def dispatch_caller(self, caller):
        ...

    def dispatch_call(self, call):
        ...
