class Lion:
    def __init__(self, state):
        if state != "сытый" and state != "голодный":
            raise ValueError("Нет такого состояния")
        self.state = state
        self.act = "спать"

    def work(self, event):
        if event == "антилопа":
            if self.state == "сытый":
                self.act = "спать"
                self.state = "голодный"
            else:
                self.act = "съесть"
                self.state = "сытый"
        elif event == "охотник":
            if self.state == "сытый":
                self.act = "убежать"
                self.state = "голодный"
            else:
                self.act = "убежать"
        elif event == "дерево":
            if self.state == "сытый":
                self.act = "смотреть"
                self.state = "голодный"
            else:
                self.act = "спать"
        else:
            raise ValueError("Неверное входное значение")

    def __str__(self):
        return '%s, %s' % (self.act, self.state)