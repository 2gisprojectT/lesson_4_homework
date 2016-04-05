class Lion:
    def __init__(self,state):
        if state.lower() == "голодный" or state.lower() == "сытый":
            self.state = state.lower()
        else:
            self.state = None

    def transition(self, symbol):
        symbol = symbol.lower()
        if symbol == "антилопа":
            self.__antelope()
        elif symbol == "охотник":
            self.__hunter()
        elif symbol == "дерево":
            self.__tree()
        else:
            return "Неверный входной символ"

    def __antelope(self):
        if self.state == "голодный":
            self.state = "сытый"
            self.action = "съесть"
        elif self.state == "сытый":
            self.state = "голодный"
            self.action = "спать"

    def __hunter(self):
        if self.state == "голодный":
            self.action = "убежать"
        elif self.state == "сытый":
            self.state = "голодный"
            self.action = "убежать"

    def __tree(self):
        if self.state == "голодный":
            self.state = "голодный"
            self.action = "спать"
        elif self.state == "сытый":
            self.state = "голодный"
            self.action = "смотреть"
