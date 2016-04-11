class EventException(Exception):
    pass


class HungryException(Exception):
    pass


class Lion(object):
    def __init__(self, event, condition):
        self.__condition = condition
        self.__event = event
        self.__check_constructor()

    def __check_constructor(self):
        if self.__condition == "Голодный" or self.__condition == "Сытый":
            pass
        else:
            raise HungryException("Неверный параметр %s вместо Сытый/ Голодный" % self.__condition)
        if self.__event == "Антилопа" or self.__event == "Охотник" or self.__event == "Охотник":
            pass
        else:
            raise EventException("Неверный параметр %s вместо Дерево/ Охотник/ Антилопа" % self.__event)

    def add_event(self, event):
        self.__event = event

    def launch(self):
        if self.__condition == "Голодный":
            self.__hungry()
        elif self.__condition == "Сытый":
            self.__not_hungry()

    def __hungry(self):
        if self.__event == "Антилопа":
            self.__action = "Съесть"
            self.__condition = "Сытый"
        elif self.__event == "Охотник":
            self.__action = "Бежать"
        elif self.__event == "Дерево":
            self.__action = "Спать"

    def __not_hungry(self):
        self.__condition = "Голодный"
        if self.__event == "Антилопа":
            self.__action = "Спать"
        elif self.__event == "Охотник":
            self.__action = "Бежать"
        elif self.__event == "Дерево":
            self.__action = "Смотреть"

    def get_condition(self):
        return self.__condition

    def get_event(self):
        return self.__event

    def get_action(self):
        return self.__action
