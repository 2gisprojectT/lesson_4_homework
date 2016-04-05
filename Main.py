class EventException(Exception):
    pass


class Lion(object):
    def __init__(self, event, condition):
        self.condition = condition
        self.event = event
        self.change_state()

    def introduce_new_event(self, event):
        self.event = event
        self.change_state()

    def change_state(self):
        if self.condition == "Голодный":
            self.hungry()
        elif self.condition == "Сытый":
            self.not_hungry()
        else:
            raise ValueError("Неверный параметр Сытый / Голодный")

    def hungry(self):
        if self.event == "Антилопа":
            self.action = "Съесть"
            self.condition = "Сытый"
        elif self.event == "Охотник":
            self.action = "Бежать"
        elif self.event == "Дерево":
            self.action = "Спать"
        else:
            raise EventException("Неверный параметр события")

    def not_hungry(self):
        self.condition = "Голодный"
        if self.event == "Антилопа":
            self.action = "Спать"
        elif self.event == "Охотник":
            self.action = "Бежать"
        elif self.event == "Дерево":
            self.action = "Смотреть"
        else:
            raise EventException("Неверный параметр события")
