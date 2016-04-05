
class LionStateFSM:

    # Инициализируем льва с определенным состоянием
    def __init__(self, state):
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise ValueError("Нет такого состояния: ", state)
        self.obj_list = ['антилопа', 'охотник', 'дерево']
        self.state_list = [
                            ['антилопа', 'сытый', 'спать', 'голодный'],
                            ['антилопа', 'голодный', 'съесть', 'сытый'],
                            ['охотник', 'сытый', 'убежать', 'голодный'],
                            ['охотник', 'голодный', 'убежать', 'голодный'],
                            ['дерево', 'сытый', 'смотреть', 'голодный'],
                            ['дерево', 'голодный', 'спать', 'голодный']
                         ]
        self.action = ""

    # Реализация методов конечного автомата состояния льва
    # Сравниваем входной объек и состояние льва с объектами и состояниями списка
    # Если находим совпадение осуществляем действие и переходим в новое состояние
    def fsm_realisation(self, obj):
        n = 0
        while n < len(self.state_list):
            if obj == self.state_list[n][0] and self.state == self.state_list[n][1]:
                self.action = self.state_list[n][2]
                self.state = self.state_list[n][3]
                print("Исходное_состояние: " + self.state_list[n][1] + " | Объект: " + obj + " | Действие: " + self.action + " | Новое_Состояние :" + self.state)
                break
            n += 1
        if n == len(self.state_list):
            raise ValueError("Вы ввели неверный объект! Нет такой комбинации состояние + объект")
                
