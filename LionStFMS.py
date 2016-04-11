states = ['сытый', 'голодный']
objects = ['антилопа', 'охотник', 'дерево']
actions = ['съесть', 'спать', 'убежать', 'смотреть']


class LionStateFSM:
    def __init__(self, state):
        self.state_list = {
                            states[0]: {
                                        objects[0]: [actions[1], states[1]],
                                        objects[1]: [actions[2], states[1]],
                                        objects[2]: [actions[3], states[1]]
                                       },
                            states[1]: {
                                        objects[0]: [actions[0], states[0]],
                                        objects[1]: [actions[2], states[1]],
                                        objects[2]: [actions[1], states[1]]
                                    }
                        }
        if state in self.state_list:
            self.state = state
        else:
            raise ValueError("Нет такого состояния: ", state)
        self.action = ""

    def fsm_realisation(self, obj):
        if obj not in self.state_list[self.state]:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
        self.action = self.state_list[self.state][obj][0]
        self.state = self.state_list[self.state][obj][1]
