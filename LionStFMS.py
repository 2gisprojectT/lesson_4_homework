
class LionStateFSM:
    objects_list = ["антилопа", "охотник", "дерево"]

    # Инициализируем льва с определенным состоянием
    def __init__(self, state):
        if state == "сытый" or state == "голодный":
            self.state = state.lower()
        else:
            raise NameError("Нет такого состояния")
        self.action = ""

    # Реализация конечного автомата состояния льва
    def fsm_realisation(self, obj):
        print("Исходное состояние :" + self.state)
        if obj == "антилопа":
            if self.state == "сытый":
                self.action = "спать"
                self.state = "голодный"
            else:
                self.action = "съесть"
                self.state = "сытый"
        if obj == "охотник":
            if self.state == "сытый":
                self.action = "убежать"
                self.state = "голодный"
            else:
                self.action = "убежать"
        if obj == "дерево":
            if self.state == "сытый":
                self.action = "смотреть"
                self.state = "голодный"
            else:
                self.action = "спать"
        print("Объект: " + obj + "| Действие: " + self.action + "| Новое_Состояние :" + self.state)

    # Запуск FMS для всех возможных объектов в нескольких циклах
    def lion_fms_work(self):
        n = 0
        while n < 3:
            for obj in self.objects_list:
                self.fsm_realisation(obj)
            n += 1
