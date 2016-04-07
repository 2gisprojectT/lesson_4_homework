
class LionStateFSM:

    def __init__(self, state):
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
        if state in self.state_list:
            self.state = state
        else:
            raise ValueError("Нет такого состояния: ", state)
        self.action = ""

    def fsm_realisation(self, obj):
        if obj in self.state_list[self.state]:
            print("Исходное_состояние: " + self.state + " | Объект: " + obj + " | Действие: " +
                  self.state_list[self.state][obj][0] + " | Новое_Состояние :" + self.state_list[self.state][obj][1])
            self.action = self.state_list[self.state][obj][0]
            self.state = self.state_list[self.state][obj][1]
        else:
            raise ValueError("Вы ввели не верный объект! Нет такой комбинации состояние + объект")
                
