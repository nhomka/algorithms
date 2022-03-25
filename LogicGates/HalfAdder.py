from LogicGate import FeedGate, AndGate, XorGate
from Connector import Connector

class HalfAdder():
    
    def __init__(self, feed1, feed2):
        fg0 = FeedGate("feed_gate_0", feed1)
        fg1 = FeedGate("feed_gate_1", feed2)
        and_gate = AndGate("and_gate")
        xor_gate = XorGate("xor_gate")

        ca1 = Connector(fg0, and_gate)
        ca2 = Connector(fg1, and_gate)
        ca3 = Connector(fg0, xor_gate)
        ca4 = Connector(fg1, xor_gate)

        c = and_gate.get_output()
        s = xor_gate.get_output()

        print(f"inputs = {feed1}, {feed2}, sum = {s}, carry = {c}")

_ = HalfAdder(0, 0)
_ = HalfAdder(0, 1)
_ = HalfAdder(1, 0)
_ = HalfAdder(1, 1)