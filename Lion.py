class Lion:
    def __init__(self, state):
        if state.lower() == "сытый" or state.lower() == "голодный":
            self.state = state.lower()
        else:
            raise ValueError("Неверное состояние")
        self.action = ""

    def input_object(self, object):
        if self.state == "сытый":
            if object.lower() == "антилопа":
                self.state = "голодный"
                self.action = "спать"
            elif object.lower() == "охотник":
                self.action = "убежать"
                self.state = "голодный"
            elif object.lower() == "дерево":
                self.action = "смотреть"
                self.state = "голодный"
            else:
                raise ValueError("Неверный объект")
        elif self.state == "голодный":
            if object.lower() == "антилопа":
                self.action = "съесть"
                self.state = "сытый"
            elif object.lower() == "охотник":
                self.action = "убежать"
            elif object.lower() == "дерево":
                self.action = "спать"
            else:
                raise ValueError("Неверный объект")
