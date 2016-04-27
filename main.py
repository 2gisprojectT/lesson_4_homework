"""
Структура словаря имеет вид:
    {<состояние>:<символ>:{"action":<действие>,"состояние":<новое состояние>}
"""
lion = {"голодный":
            {"антилопа": {"action": "съесть", "state": "сытый"},
             "охотник": {"action": "убежать", "state": "голодный"},
             "дерево": {"action": "спать", "state": "голодный"}},
        "сытый":
            {"антилопа": {"action": "спать", "state": "голодный"},
             "охотник": {"action": "убежать", "state": "голодный"},
             "дерево": {"action": "смотреть", "state": "голодный"}}}


class FSM:
    def __init__(self, dictionary, state):
        if not state in dictionary.keys():
            raise ValueError("Состояния нет в словаре переходов")
        else:
            self.dictionary = dictionary
            self.state = state
            self.action = ""

    def input(self, symbol):
        if not symbol in self.dictionary[self.state].keys():
            raise ValueError('Входного символа нет в словаре переходов')
        else:
            self.action = self.dictionary[self.state][symbol]['action']
            self.state = self.dictionary[self.state][symbol]['state']
