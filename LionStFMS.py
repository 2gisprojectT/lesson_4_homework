
class LionStateFSM:

    def __init__(self, obj, state):
        if obj == "антилопа" or obj == "охотник" or obj == "дерево":
            self.obj = obj.lower()
        else:
            raise NameError("Нет такого объекта")
        if state == "сытый" or state == "голодный":
            self.state = state.lower()
        else:
            raise NameError("Нет такого состояния")
        self.action = ""

    def fsm_realisation(self):
        print("Исходное состояние :" + self.state)
        if self.obj == "антилопа":
            if self.state == "сытый":
                self.action = "спать"
                self.state = "голодный"
            else:
                self.action = "съесть"
                self.state = "сытый"
        if self.obj == "охотник":
            if self.state == "сытый":
                self.action = "убежать"
                self.state = "голодный"
            else:
                self.action = "убежать"

        if self.obj == "дерево":
            if self.state == "сытый":
                self.action = "смотреть"
                self.state = "голодный"
            else:
                self.action = "спать"
        print("Объект: " + self.obj + "| Действие: " + self.action + "| Новое_Состояние :" + self.state)
