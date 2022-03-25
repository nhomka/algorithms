class Connector:

    def __init__(self, from_gate, to_gate):
        self.from_gate = from_gate
        self.to_gate = to_gate

        to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate
    
    def get_to(self):
        return self.to_gate