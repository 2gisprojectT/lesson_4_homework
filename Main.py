class autoLion(object):
    def __init__(self, input, status):
        self.input = input
        self.status = status

    def funinput(self,input):
         self.input = input
         self.check()

    def check(self):

        if self.input == "охотник" and (self.status == "голодный" or self.status == "сытый"):
            self.action = "убежать"
            self.status = "голодный"

        elif self.input == "дерево" and self.status == "голодный":
            self.action = "спать"
            self.status = "голодный"

        elif self.input == "дерево" and self.status == "сытый":
            self.action = "смотреть"
            self.status = "голодный"

        elif self.input == "антилопа" and self.status == "голодный":
            self.action = "съесть"
            self.status = "сытый"

        elif self.input == "антилопа" and self.status == "сытый":
            self.action = "спать"
            self.status = "голодный"
        else:
            if self.status == "сытый":
                self.action = "Неверно введены входные данные"
            elif self.status == "голодный":
                self.action = "Неверно введены входные данные"
            else:
                self.status = "Неверно введено состояние"
                self.action = "Неверно введено состояние"
