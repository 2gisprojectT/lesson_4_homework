class Lion:
    def __init__(self, state, trans_table):
        state = state.lower()
        if state not in trans_table:
            raise ValueError("Неверное внутреннее состояние ", state)
        self.state = state
        self.trans_table = trans_table
        self.action = ""

    def transition(self, symbol):
        symbol = symbol.lower()
        if symbol not in self.trans_table[self.state]:
            raise ValueError("Неверный входной символ ", symbol)
        self.action = self.trans_table[self.state][symbol]['action']
        self.state = self.trans_table[self.state][symbol]['state']
