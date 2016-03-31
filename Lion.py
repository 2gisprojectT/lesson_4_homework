class Lion:
    def __init__(self, state):
        self.state = state.lower()
        self.action = ""
        self.err = ""

    def act(self, event):
        temp_event = event.lower()
        if temp_event == "антилопа":
            self.antelope()
        elif temp_event == "охотник":
            self.hunter()
        elif temp_event == "дерево":
            self.tree()
        else:
            self.error("события")

    def antelope(self):
        if self.state == "сытый":
            self.action = "спать"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "съесть"
            self.state = "сытый"
        else:
            self.error("состояния")

    def hunter(self):
        if self.state == "сытый":
            self.action = "убежать"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "убежать"
        else:
            self.error("состояния")

    def tree(self):
        if self.state == "сытый":
            self.action = "смотреть"
            self.state = "голодный"
        elif self.state == "голодный":
            self.action = "спать"
        else:
            self.error("состояния")

    def error(self, err):
        self.err = "ошибка " + err

