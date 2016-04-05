class Lion:
    def __init__(self, state):
        self.action = ""
        if state.lower() == "сытый" or state.lower() == "голодный":
            self.state = state
        else:
            raise ValueError("Неверное состояние!")

    def act(self, event):
        temp_event = event.lower()
        if temp_event == "антилопа":
            self.__antelope()
        elif temp_event == "охотник":
            self.__hunter()
        elif temp_event == "дерево":
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
        else:
            raise ValueError("Неверное состояние!")

    def __hunter(self):
        if self.state == "сытый":
            self.action = "убежать"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "убежать"
        else:
            raise ValueError("Неверное состояние!")

    def __tree(self):
        if self.state == "сытый":
            self.action = "смотреть"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "спать"
        else:
            raise ValueError("Неверное состояние!")

