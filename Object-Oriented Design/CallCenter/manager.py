from CallCenter.employee import Employee


class Manager(Employee):
    def __init__(self):
        super.__init__()
        self.rank = 1
