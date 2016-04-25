class Lion:
    def __init__(self, state="сытый", act="спать"):
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise Exception("Нет такого состояния")
        if act == "съесть" or act == "убежать" or act == "смотреть" or act == "спать":
            self.act = act
        else:
            raise Exception("Нет такого действия")

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
            raise Exception("Ерунда на входе")

    def __str__(self):
        return '%s, %s' % (self.act, self.state)