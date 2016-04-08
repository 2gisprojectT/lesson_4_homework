import sys, traceback


class Lion:
    states = ('сытый', 'голодный')
    factors = ('антилопа', 'охотник', 'дерево')

    def __init__(self, state):
        try:
            index = self.states.index(state.lower())
            self.indexState = index
        except ValueError:
            msg = "Неизвестное состояние: " + state +\
                  "\nИзвестные состояния: " + str(self.states)
            raise ValueError(msg)

    def action(self, factor):
        try:
            index = self.factors.index(factor.lower())
        except ValueError:
            msg = "Неизвестный фактор: " + factor +\
                  "\nИзвестные факторы: " + str(self.factors)
            raise ValueError(msg)
        
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
    a = Lion('сытый')
    a.action('антилопак')