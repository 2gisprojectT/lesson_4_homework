

class LionStateFSM:
    def __init__(self, state, state_list):
        if state_list is None:
            raise ValueError("Список пуст!")
        if state not in state_list:
            raise ValueError("Нет такого состояния: ", state)
        self.state_list = state_list
        self.state = state
        self.action = None

    def fsm_realisation(self, obj):
        if obj not in self.state_list[self.state]:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
        self.action = self.state_list[self.state][obj]['action']
        self.state = self.state_list[self.state][obj]['new_state']
