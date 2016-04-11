class LionStates:
    def __init__(self, state):
        state.lower()
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise ValueError("Неверное состояние !")
        self.action = ""

    def implementation_fsm(self, symbol):
        if symbol == "антилопа":
            self.__antelope()
        elif symbol == "охотник":
            self.__hunter()
        elif symbol == "дерево":
            self.__tree()
        else:
            raise ValueError("Неверный входной символ !")

    def __antelope(self):
        if self.state == "сытый":
            self.action = "спать"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "съесть"
            self.state = "сытый"

    def __hunter(self):
        if self.state == "сытый":
            self.action = "убежать"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "убежать"
            self.state = "голодный"

    def __tree(self):
        if self.state == "сытый":
            self.action = "смотреть"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "спать"
            self.state = "голодный"
