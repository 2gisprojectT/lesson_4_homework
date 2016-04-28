class FSM:
    def __init__(self, dictionary, state):
        if not state in dictionary.keys():
            raise ValueError("Состояния нет в словаре переходов")
        self.dictionary = dictionary
        self.state = state
        self.action = None

    def input(self, symbol):
        if not symbol in self.dictionary[self.state].keys():
            raise ValueError('Входного символа нет в словаре переходов')
        self.action = self.dictionary[self.state][symbol]['action']
        self.state = self.dictionary[self.state][symbol]['state']
