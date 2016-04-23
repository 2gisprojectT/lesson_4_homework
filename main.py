class Lion:
    def __init__(self, state, table):
        if not (state in table.keys()):
            raise ValueError("Задаваемого состояния нет в таблице переходов: %s" % state)
        self._table = table.copy()
        self.state = state
        self.action = None

    def input(self, obj):
        transition = self._table[self.state].get(obj)
        if transition is None:
            raise ValueError("Не верный входной символ: %s" % obj)
        self.action = transition[1]
        self.state = transition[0]
