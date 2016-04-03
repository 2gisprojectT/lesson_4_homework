from enum import Enum


class Lion:
    def __new__(cls,state):
        if state.upper()=="СЫТЫЙ" or state.upper()=="ГОЛОДНЫЙ":
            return super(Lion,cls).__new__(cls);
        else:
            return None;
    def __init__(self,state):
        self.state=state.upper();
    def input(self,obj):
        if self.state=="СЫТЫЙ":
            if obj.upper()=="АНТИЛОПА":
                self.action="Спать";
            elif obj.upper()=="ОХОТНИК":
                self.action="Убежать";
            elif obj.upper()=="ДЕРЕВО":
                self.action="Смотреть";
            else:
                return "Неверный символ";
            self.state="ГОЛОДНЫЙ";
        elif self.state=="ГОЛОДНЫЙ":
            if obj.upper()=="АНТИЛОПА":
                self.action="Съесть";
                self.state="СЫТЫЙ";
            elif obj.upper()=="ОХОТНИК":
                self.action="Убежать";
            elif obj.upper()=="ДЕРЕВО":
                self.action="Спать";
            else:
                return "Неверный символ";