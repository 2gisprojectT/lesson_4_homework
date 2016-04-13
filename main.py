class Lion:
    def __init__(self, state):
        if state.upper() == "ГОЛОДНЫЙ":
            self.state = "ГОЛОДНЫЙ"
        else:
            self.state = "СЫТЫЙ"
        self.__table = {("АНТИЛОПА", "СЫТЫЙ"): ("ГОЛОДНЫЙ", "Спать"), ("АНТИЛОПА", "ГОЛОДНЫЙ"): ("СЫТЫЙ", "Съесть"),
                        ("ОХОТНИК", "СЫТЫЙ"): ("ГОЛОДНЫЙ", "Убежать"), ("ОХОТНИК", "ГОЛОДНЫЙ"): ("ГОЛОДНЫЙ", "Убежать"),
                        ("ДЕРЕВО", "СЫТЫЙ"): ("ГОЛОДНЫЙ", "Смотреть"), ("ДЕРЕВО", "ГОЛОДНЫЙ"): ("ГОЛОДНЫЙ", "Спать")}
        self.action = None

    def input(self, obj):
        transition = self.__table.get((obj.upper(), self.state))
        if transition is not None:
            self.action = transition[1]
            self.state = transition[0]
        else:
            return "Неверный символ"
