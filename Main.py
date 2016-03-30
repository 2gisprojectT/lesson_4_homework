class EventException(Exception):
    pass


class Lion(object):
    def __init__(self, event, condition):
        self.condition = condition
        self.event = event
        self.action = ""
        self.isHungry()

    def isHungry(self):
        if self.condition == "Голодный":
            self.Hungry()
        elif self.condition == "Сытый":
            self.notHungry()
        else:
            raise ValueError("Неверный параметр Сытый / Голодный")

    def Hungry(self):
        if self.event == "Антилопа":
            self.action = "Съесть"
            self.condition = "Сытый"
        elif self.event == "Охотник":
            self.action = "Бежать"
        elif self.event == "Дерево":
            self.action = "Спать"
        else:
            raise EventException("Неверный параметр события")

    def notHungry(self):
        self.condition = "Голодный"
        if self.event == "Антилопа":
            self.action = "Спать"
        elif self.event == "Охотник":
            self.action = "Бежать"
        elif self.event == "Дерево":
            self.action = "Смотреть"
        else:
            raise EventException("Неверный параметр события")
