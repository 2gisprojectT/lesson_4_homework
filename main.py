class Lion:
    def __init__(self, state, table):
        self._table = dict()
        for cell in table:
            self._table[(cell[0].upper(), cell[1].upper())] = (table[cell][0].upper(), table[cell][1])
        states = {key[1] for key in self._table.keys()}
        states = states.union({val[0] for val in self._table.values()})
        if state.upper() in states:
            self.state = state.upper()
        else:
            raise ValueError("Задаваемого состояния нет в таблице переходов: %s" % state)
        self.action = None

    def input(self, obj):
        transition = self._table.get((obj.upper(), self.state))
        if transition is not None:
            self.action = transition[1]
            self.state = transition[0]
        else:
            raise ValueError("Не верный входной символ: %s" % obj)
