'''Plab 2 Gruppe 20'''


# A rule object should contain at least these four instance variables:
# 1. state1 - triggering state of the FSM
# 2. state2 - new state of the FSM if this rule fires
# 3. signal - triggering signal
# 4. action - the agent will be instructed to perform this action if this rule fires.


class Rule:
    """Rule class to control trasitions between states"""

    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action

    def check_rule(self, current_state, current_signal):
        '''Checks if a rule is to be fired'''
        # current_signal - the signal that comes from the FSM
        # current_signal - the current state that the FSM is in
        return current_state == self.state1 and current_signal in self.signal
