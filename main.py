class Lion:
    def __init__(self, state_init):
        if state_init != "голодный" and state_init != "сытый":
            raise ValueError
        else:
            self.state = state_init

    def behaving(self, object):
        if object == "антилопа":
            if self.state == "голодный":
                action = "съесть"
                self.state = "сытый"
            else:
                action = "спать"
                self.state = "голодный"
            return action + " " + self.state
        elif object == "охотник":
            action = "убежать"
            if self.state == "сытый":
                self.state = "голодный"
            return action + " " + self.state
        elif object == "дерево":
            if self.state == "голодный":
                action = "спать"
            else:
                action = "смотреть"
                self.state = "голодный"
            return action + " " + self.state
        else:
            return "данного объекта не предусмотрено"
