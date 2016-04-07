import sys, traceback


class Lion:
    states = ('сытый', 'голодный')
    factors = ('антилопа', 'охотник', 'дерево')

    def __init__(self, state):
            index = self.states.index(state.lower())
            self.indexState = index

    def action(self, factor):
        index = self.factors.index(factor.lower())
        if index == 0:
            action = ['съесть', 'спать'][self.indexState == 0]
            self.indexState = (self.indexState + 1) % 2
            return action
        elif index == 1:
            self.indexState = 1
            return 'убежать'
        else:
            action = ['спать', 'смотреть'][self.indexState == 0]
            self.indexState = 1
            return action

    def get_state(self):
        return self.states[self.indexState]

if __name__ == "__main__":
    Lion('asda')