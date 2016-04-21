class Lion:
    def __init__(self, state, table):
        self._table = table
        states = {key[1] for key in self._table.keys()}
        states = states.union({val[0] for val in self._table.values()})
        if not (state in states):
            raise ValueError("Задаваемого состояния нет в таблице переходов: %s" % state)
        self.state = state
        self.action = None

    def input(self, obj):
        transition = self._table.get((obj, self.state))
        if transition is None:
            raise ValueError("Не верный входной символ: %s" % obj)
        self.action = transition[1]
        self.state = transition[0]
