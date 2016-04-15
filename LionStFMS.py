class LionStateFSM:
    def __init__(self, state):
        self.state_list = {
                            'сытый': {
                                        'антилопа': {'action': 'спать', 'new_state': 'голодный'},
                                        'охотник': {'action': 'убежать', 'new_state': 'голодный'},
                                        'дерево': {'action': 'смотреть', 'new_state': 'голодный'}
                                       },
                            'голодный': {
                                        'антилопа': {'action': 'съесть', 'new_state': 'голодный'},
                                        'охотник': {'action': 'убежать', 'new_state': 'голодный'},
                                        'дерево': {'action': 'спать', 'new_state': 'голодный'}
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
        self.state = self.state_list[self.state][obj]['new_state']
