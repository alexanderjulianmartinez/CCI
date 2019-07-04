from CallCenter.employee import Employee


class Director(Employee):
    def __init__(self):
        super.__init__()
        self.rank = 2
