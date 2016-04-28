class Lion:
    def __init__(self, state):
        if not state.lower() == "сытый" and not state.lower() == "голодный":
            raise ValueError("Неверное состояние!")

        self.action = ""
        self.state = state

    def act(self, action):
        event = action.lower()
        if event == "антилопа":
            self.__antelope()
        elif event == "охотник":
            self.__hunter()
        elif event == "дерево":
            self.__tree()
        else:
            raise ValueError("Неверное событие!")

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

    def __tree(self):
        if self.state == "сытый":
            self.action = "смотреть"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "спать"

