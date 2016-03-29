class LionStates:
    def __init__(self, state, symbol):
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise ValueError("Неверное состояние !")

        if symbol == "антилопа" or symbol == "охотник" or symbol == "дерево":
            self.symbol = symbol
        else:
            raise ValueError("Неверный входной символ !")

        self.action = ""

    def implementation_fsm(self):
        if self.state == "сытый":
            if self.symbol == "антилопа":
                self.action = "спать"
                self.state = "голодный"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

            elif self.symbol == "охотник":
                self.action = "убежать"
                self.state = "голодный"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

            elif self.symbol == "дерево":
                self.action = "смотреть"
                self.state = "голодный"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

        elif self.state == "голодный":
            if self.symbol == "антилопа":
                self.action = "съесть"
                self.state = "сытый"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

            elif self.symbol == "охотник":
                self.action = "убежать"
                self.state = "голодный"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())

            elif self.symbol == "дерево":
                self.action = "спать"
                self.state = "голодный"
                print("Действие: " + self.action.upper() + ", текущее состояние: " + self.state.upper())