class Lion:
    def __init__(self, state):
        self.states = ["сытый", "голодный"]
        self.symbols = ["антилопа", "охотник", "дерево"]
        self.trans_table_actions = [["спать", "съесть"], ["убежать", "убежать"], ["смотреть", "спать"]]
        self.trans_table_states = [["голодный", "сытый"], ["голодный", "голодный"], ["голодный", "голодный"]]
        self.action = ""
        if state.lower() in self.states:
            self.state = state.lower()
        else:
            self.state = self.states[0]
            raise ValueError("Неверное внутреннее состояние ", state)

    def transition(self, symbol):
        symbol = symbol.lower()
        if symbol in self.symbols:
            self.action = self.trans_table_actions[self.symbols.index(symbol)][self.states.index(self.state)]
            self.state = self.trans_table_states[self.symbols.index(symbol)][self.states.index(self.state)]
        else:
            raise ValueError("Неверный входной символ ", symbol)