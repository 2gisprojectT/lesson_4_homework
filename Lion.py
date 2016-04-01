class Lion:
    def __init__(self, condition):
        self.state = condition.lower()

    def action(self, symbol):
        symbol = symbol.lower()
        if symbol == "антилопа":
            return self.antelope()
        if symbol == "охотник":
            return self.hunter()
        if symbol == "дерево":
            return self.tree()
        else:
            return "?"

    def antelope(self):
        if self.state == "голодный":
            self.state = "сытый"
            return "съесть"
        if self.state == "сытый":
            self.state = "голодный"
            return "спать"

    def hunter(self):
        if self.state == "голодный":
            return "убежать"
        if self.state == "сытый":
            self.state = "голодный"
            return "убежать"

    def tree(self):
        if self.state == "голодный":
                self.state = "голодный"
                return "спать"
        if self.state == "сытый":
                self.state = "голодный"
                return "смотреть"