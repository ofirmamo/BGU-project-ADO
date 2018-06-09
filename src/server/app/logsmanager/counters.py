

class Counters:

    def __init__(self):
        self.total_transaction: int = 0
        self.injected_trans: int = 0
        self.injected_caught: int = 0
        self.falsely_caught: int = 0
        self.ratio: int = 0

    def clear(self):
        self.total_transaction: int = 0
        self.injected_trans: int = 0
        self.injected_caught: int = 0
        self.falsely_caught: int = 0
        self.ratio: int = 0
