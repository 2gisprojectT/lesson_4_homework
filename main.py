class Lion:
    def __init__(self, state_init):
        if state_init != "голодный" and state_init != "сытый":
            raise ValueError("невозможное состояние")
        self.state = state_init
        self.action = ""

    def behaving(self, obj):
        if obj == "антилопа":
            if self.state == "голодный":
                self.action = "съесть"
                self.state = "сытый"
            else:
                self.action = "спать"
                self.state = "голодный"
        elif obj == "охотник":
            self.action = "убежать"
            if self.state == "сытый":
                self.state = "голодный"
        elif obj == "дерево":
            if self.state == "голодный":
                self.action = "спать"
            else:
                self.action = "смотреть"
                self.state = "голодный"
        else:
            raise ValueError("нераспознанный объект")
