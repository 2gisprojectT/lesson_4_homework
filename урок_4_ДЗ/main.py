class Lion:
    def __init__(self):
        self.state = "голодный"
    def behaving(self, object):
        if object == "антилопа":
            if self.state == "голодный":
                print("съесть")
                self.state="сытый"
            else:
                print("спать")
                self.state = "голодный"
            print("стал " + self.state)
        elif object == "охотник":
            print("убежать")
            if self.state == "сытый":
                self.state = "голодный"
            print("стал " + self.state)
        elif object == "дерево":
            if self.state == "голодный":
                print("спать")
            else:
                print("смотреть")
                self.state = "голодный"
            print("стал " + self.state)
        else:
            print("данного объекта не предусмотрено")


lion = Lion()
lion.behaving("дерево")
lion.behaving("пыпп")
lion.behaving("антилопа")