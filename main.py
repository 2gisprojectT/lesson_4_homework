from enum import Enum


class Lion:
    def __init__(self,state):
        self.err=0;
        if state.upper()=="СЫТЫЙ" or state.upper()=="ГОЛОДНЫЙ":
            self.state=state.upper();
        else:
            self.err="Неверный входной параметр";
    def input(self,obj):
        if (self.err==0):
            if self.state=="СЫТЫЙ":
                if obj.upper()=="АНТИЛОПА":
                    self.action="Спать";
                elif obj.upper()=="ОХОТНИК":
                    self.action="Убежать";
                elif obj.upper()=="ДЕРЕВО":
                    self.action="Смотреть";
                else:
                    self.err="Неверный символ";
                    return;
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
                    self.err="Неверный символ";
                    return;
        return;