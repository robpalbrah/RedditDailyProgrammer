state_transitions = [('S0', 'S1', 'white'),
                     ('S0', 'S2', 'red'),
                     ('S1', 'S2', 'white'),
                     ('S1', 'S3', 'orange'),
                     ('S2', 'S0', 'red'),
                     ('S2', 'S3', 'black'),
                     ('S3', 'S3', 'black'),
                     ('S3', 'S4', 'orange'),
                     ('S3', 'S5', 'green'),
                     ('S4', 'S6', 'green'),
                     ('S5', 'S6', 'orange')]

class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None
        self.start_state = None
        self.finish_state = None

    def add_state(self, state):
        if state not in self.states:
            self.states[state] = {}

    def set_start_state(self, state):
        self.start_state = state
        self.add_state(state)

    def set_finish_state(self, state):
        self.finish_state = state
        self.add_state(state)

    def add_transition(self, from_state, to_state, trigger):
        self.states[from_state][trigger] = to_state

    def change_state(self, trigger):
        try:
            self.current_state = self.states[self.current_state][trigger]
        except KeyError:
            print("{} is not a valid transition from state {}".format(
                trigger, self.current_state))

class Bomb(StateMachine):
    def __init__(self, state_transitions):
        StateMachine.__init__(self)
        for i in range(7):
            self.add_state("S{}".format(i))
        self.set_start_state("S0")
        self.set_finish_state("S6")
        self.current_state = self.start_state
        for transition in state_transitions:
            self.add_transition(*transition)

    def change_state(self, trigger):
        try:
            self.current_state = self.states[self.current_state][trigger]
        except KeyError:
            return False
        return True

    def cut_wires(self, wires):
        for wire in wires:
            if not self.change_state(wire):
                return False
                break
        else:
            if self.finish_state == self.current_state:
                return True

if __name__ == '__main__':
    import unittest

    bomb = Bomb(state_transitions)
    wires_0 = ["white", "white", "red", "white", "orange", "black", "black", "green", "orange"]
    wires_1 = ['white', 'white', 'red', 'red', 'red', 'white', 'white', 'black', 'green', 'orange']
    wires_2 = ['white', 'black', 'black', 'black', 'black', 'green', 'orange']
    wires_3 = ['white', 'white', 'green', 'orange', 'green']
    wires_4 = ['black', 'green', 'green']
    wires_5 = ['red', 'red', 'white', 'orange', 'black', 'green']

    class TestBomb(unittest.TestCase):
        def test_cut_wires(self):
            self.assertTrue(bomb.cut_wires(wires_1))
            self.assertFalse(bomb.cut_wires(wires_2))
            self.assertFalse(bomb.cut_wires(wires_3))
            self.assertFalse(bomb.cut_wires(wires_4))
            self.assertFalse(bomb.cut_wires(wires_5))

    unittest.main()
