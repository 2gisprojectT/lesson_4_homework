states = ['сытый', 'голодный']
objects = ['антилопа', 'охотник', 'дерево']
actions = ['съесть', 'спать', 'убежать', 'смотреть']


class LionStateFSM:
    def __init__(self, state):
        self.state_list = {
                            states[0]: {
                                        objects[0]: {'action': actions[1], 'state': states[1]},
                                        objects[1]: {'action': actions[2], 'state': states[1]},
                                        objects[2]: {'action': actions[3], 'state': states[1]}
                                       },
                            states[1]: {
                                        objects[0]: {'action': actions[0], 'state': states[0]},
                                        objects[1]: {'action': actions[2], 'state': states[1]},
                                        objects[2]: {'action': actions[1], 'state': states[1]}
                                    }
                        }
        if state not in self.state_list:
            raise ValueError("Нет такого состояния: ", state)
        self.state = state
        self.action = ""

    def fsm_realisation(self, obj):
        if obj not in self.state_list[self.state]:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
        self.action = self.state_list[self.state][obj]['action']
        self.state = self.state_list[self.state][obj]['state']
