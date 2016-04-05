
class LionStateFSM:
    objects_list = ["антилопа", "охотник", "дерево", "охотник", "антилопа", "дерево"]

    # Инициализируем льва с определенным состоянием
    def __init__(self, state):
        if state == "сытый" or state == "голодный":
            self.state = state
        else:
            raise ValueError("Нет такого состояния: ", state)
        self.lion_list = [
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
        while n < len(self.lion_list):
            if obj == self.lion_list[n][0] and self.state == self.lion_list[n][1]:
                self.action = self.lion_list[n][2]
                self.state = self.lion_list[n][3]
                print("Исходное состояние: " + self.lion_list[n][1] + " | Объект: " + obj + " | Действие: " + self.action + " | Новое_Состояние :" + self.state)
                break
            n += 1
        if n == len(self.lion_list):
            raise ValueError("Нет такой комбинации состояния: {0} + объект: {1}".format(self.state, obj))

    # Запуск FMS для всех объектов из списка objects_list
    def lion_fsm_work(self):
        for obj in self.objects_list:
                self.fsm_realisation(obj)
                
