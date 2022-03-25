from cgi import print_arguments
from Connector import Connector
class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None
        
    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output

class UnaryLogicGate(LogicGate):

    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        if self.pin:
            return self.pin.get_from().get_output()
        else:
            return int(input(f"Enter pin input for gate {self.get_label()}: "))

    def set_next_pin(self, source):
        if not self.pin:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class FeedLogicGate(LogicGate):

    def __init__(self, label, pin):
        super().__init__(label)
        self.pin = pin

    def get_pin(self):
        return int(self.pin)

    def set_next_pin(self, source):
        if not self.pin:
            self.pin = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class BinaryLogicGate(LogicGate):

    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a:
            return self.pin_a.get_from().get_output() 
        else:
            return int(input(f"Enter pin A input for gate {self.get_label()}: "))

    def get_pin_b(self):
        if self.pin_b:
            return self.pin_b.get_from().get_output() 
        else:
            return int(input(f"Enter pin B input for gate {self.get_label()}: "))

    def set_next_pin(self, source):
        if not self.pin_a:
            self.pin_a = source
        elif not self.pin_b:
            self.pin_b = source
        else:
            raise RuntimeError("Error: No Empty Pins")

class AndGate(BinaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = super().get_pin_a()
        b = super().get_pin_b()
        return a and b

class OrGate(BinaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = super().get_pin_a()
        b = super().get_pin_b()
        return a or b

class XorGate(BinaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = super().get_pin_a()
        b = super().get_pin_b()
        return a ^ b

class NorGate(BinaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = super().get_pin_a()
        b = super().get_pin_b()
        return not a or not b

class NandGate(BinaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        a = super().get_pin_a()
        b = super().get_pin_b()
        return not a and not b

class NotGate(UnaryLogicGate):

    def __init__(self, label):
        super().__init__(label)

    def perform_gate_logic(self):
        return 0 if super().get_pin() else 1

class FeedGate(FeedLogicGate):

    def __init__(self, label, pin):
        super().__init__(label, pin)

    def perform_gate_logic(self):
        return super().get_pin()


# g1 = AndGate("G1")
# g2 = AndGate("G2")
# g3 = OrGate("G3")
# g4 = NotGate("G4")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)

# print(g4.get_output())

# g5 = AndGate("G5")
# g6 = AndGate("G6")
# g7 = NotGate("G7")
# g8 = NotGate("G8")
# g9 = AndGate("G9")
# c4 = Connector(g5, g7)
# c5 = Connector(g6, g8)
# c6 = Connector(g7, g9)
# c7 = Connector(g8, g9)

# print(g9.get_output())
