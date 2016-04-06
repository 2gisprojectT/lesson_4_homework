class Lion:
    def __init__(self, state_init):
        if state_init != "голодный" and state_init != "сытый":
            raise ValueError
        else:
            self.state = state_init
            self.action = ""

    def behaving(self, object):
        if object == "антилопа":
            if self.state == "голодный":
                self.action = "съесть"
                self.state = "сытый"
            else:
                self.action = "спать"
                self.state = "голодный"
        elif object == "охотник":
            self.action = "убежать"
            if self.state == "сытый":
                self.state = "голодный"
        elif object == "дерево":
            if self.state == "голодный":
                self.action = "спать"
            else:
                self.action = "смотреть"
                self.state = "голодный"
