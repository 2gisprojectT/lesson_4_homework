class EventException(Exception):
    pass


class Lion(object):
    def __init__(self, event, condition):
        self.__condition = condition
        self.__event = event

    def launch(self):
        self.__change_state()

    def add_event(self, event):
        self.__event = event

    def __change_state(self):
        if self.__condition == "Голодный":
            self.__hungry()
        elif self.__condition == "Сытый":
            self.__not_hungry()
        else:
            raise ValueError("Неверный параметр %s вместо Сытый/ Голодный" % self.__condition)

    def __hungry(self):
        if self.__event == "Антилопа":
            self.__action = "Съесть"
            self.__condition = "Сытый"
        elif self.__event == "Охотник":
            self.__action = "Бежать"
        elif self.__event == "Дерево":
            self.__action = "Спать"
        else:
            raise EventException("Неверный параметр %s вместо Дерево/ Охотник/ Антилопа" % self.__event)

    def __not_hungry(self):
        self.__condition = "Голодный"
        if self.__event == "Антилопа":
            self.__action = "Спать"
        elif self.__event == "Охотник":
            self.__action = "Бежать"
        elif self.__event == "Дерево":
            self.__action = "Смотреть"
        else:
            raise EventException("Неверный параметр %s вместо Дерево/ Охотник/ Антилопа" % self.__event)

    def get_condition(self):
        return self.__condition

    def get_event(self):
        return self.__event

    def get_action(self):
        return self.__action
