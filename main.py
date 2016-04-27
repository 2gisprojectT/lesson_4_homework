lion = {"state": {"голодный": {"symbol":
                                   {"антилопа": {"action": "съесть", "state": "сытый"},
                                    "охотник": {"action": "убежать", "state": "голодный"},
                                    "дерево": {"action": "спать", "state": "голодный"}}}},
        "state": {"сытый": {"symbol":
                                {"антилопа": {"action": "спать", "state": "голодный"},
                                 "охотник": {"action": "убежать", "state": "голодный"},
                                 "дерево": {"action": "смотреть", "state": "голодный"}}}}}


class FSM:
    def __init__(self, dictionary, state):
        if not state in dictionary["state"].keys():
            raise ValueError("Состояния нет в словаре переходов")
        else:
            self.dictionary = dictionary
            self.state = state
            self.action = ""

    def input(self, symbol):
        if not symbol in self.dictionary["state"][self.state]["symbol"].keys():
            raise ValueError('Входного символа нет в словаре переходов')
        else:
            self.action = self.dictionary["state"][self.state]["symbol"][symbol]['action']
            self.state = self.dictionary["state"][self.state]["symbol"][symbol]['state']
