from enum import Enum

class State(Enum):
    wellfed=1;
    hungry=2;

class inData(Enum):
    antilopa=1;
    hunter=2;
    tree=3;


class Lion:
    def __init__(self,state):
        self.state=state;
    def input(self,obj):
        if self.state==State.wellfed:
            if obj=="Антилопа":
                self.sleep();
            elif obj=="Охотник":
                self.run();
            elif obj=="Дерево":
                self.watch();
            else:
                return;
            self.state=State.hungry;
        if self.state==State.hungry:
            if obj=="Антилопа":
                self.eat();
                self.state=State.wellfed;
            elif obj=="Охотник":
                self.run();
                self.state=State.hungry;
            elif obj=="Дерево":
                self.sleep();
                self.state=State.hungry;
            else:
                return;

lion=Lion(State.wellfed);
print(lion.state);
