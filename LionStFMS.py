
class LionStateFSM:

    def __init__(self, state):
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise ValueError("Нет такого состояния: ", state)
        self.state_list = {
                            'сытый': {
                                'антилопа': ['спать', 'голодный'],
                                'охотник': ['убежать', 'голодный'],
                                'дерево': ['смотреть', 'голодный']
                            },
                            'голодный': {
                                'антилопа': ['съесть', 'сытый'],
                                'охотник': ['убежать', 'голодный'],
                                'дерево': ['спать', 'голодный']
                            }
                        }
        self.action = ""

    def fsm_realisation(self, obj):
        try:
            action = self.state_list[self.state][obj][0]
            state = self.state_list[self.state][obj][1]
        except Exception:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
        print("Исходное_состояние: " + self.state + " | Объект: " + obj + " | Действие: " +
              self.state_list[self.state][obj][0] + " | Новое_Состояние :" + self.state_list[self.state][obj][1])
        self.action = self.state_list[self.state][obj][0]
        self.state = self.state_list[self.state][obj][1]
                
