"""
[2016-11-21] Challenge #293 [Easy] Defusing the bomb
https://tinyurl.com/dp-293-easy
"""
# Status: Done

# allowed_wires = {cut_wire_color : [allowed_wire_color, ...], ...}
allowed_wires = {None : ['white', 'black', 'purple', 'red', 'green', 'orange'],
                 'white' : ['purple', 'red', 'green', 'orange'],
                 'black' : ['black', 'purple' 'red'],
                 'purple' : ['black', 'red'],
                 'red' : ['green'],
                 'green' : ['white', 'orange'],
                 'orange' : ['black', 'red']}

def cut_wire(wire, previous_wire = None):
    """
    Given wire and previous_wire determines whether or not you allowed
    to cut it. Returns True on success, False othervise.
    """
    if wire in allowed_wires[previous_wire]:
        return True
    else:
        return False

def process_input(input_list):
    """
    Determines whether or not you allowed to cut an ordered sequence of wires.
    Returns True on success, False otherwise. 
    """
    previous_wire = current_wire = None
    for wire in input_list:
        previous_wire = current_wire
        current_wire = wire
        if not cut_wire(current_wire, previous_wire):
            return False
    return True

def print_bomb_state(input_list):
    """
    Determines whether or not you allowed to cut an ordered sequence of wires.
    Prints "Bomb defused" on success, "Boom" otherwise.    
    """
    if process_input(input_list):
        print("Bomb defused")
    else:
        print("Boom")

if __name__ == '__main__':
    input_1 = ['white', 'red', 'green', 'white']
    input_2 = ['white', 'orange', 'green', 'white']
    print_bomb_state(input_1)
    print_bomb_state(input_2)

