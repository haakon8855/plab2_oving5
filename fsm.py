'''Plab 2 Gruppe 20'''

from Oving_5.rule import Rule
from Oving_5.agent import Agent


class FSM:
    '''FSM-class to control the finite state machine'''
    all = "#*0123456789N"

    def __init__(self, agent):
        self.current_state = "init"
        self.current_signal = None
        self.agent = agent
        self.run = True
        self.rule_list = []
        # From init
        self.add_rule("init", "read", all, "A1")
        # From read
        self.add_rule("read", "read", "0123456789", agent.a2())
        self.add_rule("read", "verify", "*", agent.verify_login()) # a3()
        self.add_rule("read", "init", all, agent.a4())
        # From verify
        self.add_rule("verify", "active", "Y", agent.a5())
        self.add_rule("verify", "init", all, agent.a4())
        # Logout process
        self.add_rule("active", "logout", "#", agent.nothing())
        self.add_rule("logout", "init", "#", agent.a4())
        self.add_rule("logout", "active", all, agent.nothing())
        # LED process
        self.add_rule("active", "led", "012345", "A12")
        self.add_rule("led", "time", "0123456789", agent.nothing())
        self.add_rule("led", "active", all, agent.a6())
        self.add_rule("time", "time", "0123456789", agent.a2())
        self.add_rule("time", "active", "*", "A10")
        self.add_rule("time", "active", all, agent.a6())
        # Password change process
        # Write password
        self.add_rule("active", "newp", "*", agent.nothing())
        self.add_rule("newp", "p1", "0123456789", agent.a2())
        self.add_rule("newp", "active", all, agent.a6())
        self.add_rule("p1", "p2", "0123456789", agent.a2())
        self.add_rule("p1", "active", all, agent.a6())
        self.add_rule("p2", "p3", "0123456789", agent.a2())
        self.add_rule("p2", "active", all, agent.a6())
        self.add_rule("p3", "p4", "0123456789", agent.a2())
        self.add_rule("p3", "active", all, agent.a6())
        self.add_rule("p4", "p4", "0123456789", agent.a2())
        self.add_rule("p4", "p4", "*", agent.a7())
        self.add_rule("p4", "active", all, agent.a6())
        # Confirm password
        self.add_rule("pc", "pc", "0123456789", agent.a2())
        self.add_rule("pc", "verify2", "*", agent.a8())
        self.add_rule("pc", "active", "#", agent.a6())
        self.add_rule("verify2", "active", "Y", agent.a11())
        self.add_rule("verify2", "active", all, agent.a6())

    def add_rule(self, state1, state2, signal, action):
        '''Adds a new rule to the end of self.rule_list'''
        rule = Rule(state1, state2, signal, action)
        self.rule_list.append(rule)

    def get_next_signal(self):
        '''Gets the next signal from the agent'''
        self.current_signal = self.agent.get_next_signal()

    def run_rules(self):
        '''Finds first satisfied rule and fires it'''
        for elem in self.rule_list:
            if self.apply_rule(elem):
                self.fire_rule(elem)
                break

    def apply_rule(self, rule):
        '''Checks if the rule is satisfied'''
        return rule.check_rule(self.current_state, self.current_signal)

    def fire_rule(self, rule):
        '''Changes the current_state, and excecutes the correct action.'''
        self.current_state = rule.state2
        rule.action()


FSM = FSM(Agent())

while FSM.run:
    FSM.get_next_signal()
    FSM.run_rules()
