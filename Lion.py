class Lion:
    def __init__(self, state, trans_table):
        if state.lower() not in trans_table:
            raise ValueError("Неверное внутреннее состояние ", state.lower())
        self.state = state.lower()
        self.trans_table = trans_table
        self.action = ""

    def transition(self, symbol):
        if symbol.lower() not in self.trans_table[self.state]:
            raise ValueError("Неверный входной символ ", symbol.lower())
        self.action = self.trans_table[self.state][symbol]['action']
        self.state = self.trans_table[self.state][symbol]['state']
