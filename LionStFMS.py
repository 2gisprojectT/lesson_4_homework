

class LionStateFSM:
    def __init__(self, state, state_list):
        if state_list['state'] != state:
            raise ValueError("Нет такого состояния: ", state)
        self.state_list = state_list
        self.state = state
        self.action = ""

    def fsm_realisation(self, obj):
        if self.state_list['object'] != obj:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
        self.action = self.state_list['action']
        self.state = self.state_list['new_state']
