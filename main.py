lion_get = {"голодный":
                {"антилопа": {"действие": "съесть", "состояние": "сытый"},
                 "охотник": {"действие": "убежать", "состояние": "голодный"},
                 "дерево": {"действие": "спать", "состояние": "голодный"}},
            "сытый":
                {"антилопа": {"действие": "спать", "состояние": "голодный"},
                 "охотник": {"действие": "убежать", "состояние": "голодный"},
                 "дерево": {"действие": "смотреть", "состояние": "голодный"}}}


class LionFSM:
    def __init__(self, state):
        if state != "голодный" and state != "сытый":
            raise ValueError("Состояние не определено")
        else:
            self.action = ""
            self.state = state

    def input(self, symbol):
        try:
            self.action = lion_get[self.state][symbol]['действие']
            self.state = lion_get[self.state][symbol]['состояние']
            return self
        except KeyError:
            return self
