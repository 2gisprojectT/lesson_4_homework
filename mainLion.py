class Lion :
    def __init__(self, state) :
        if state == "full" or state == "hungry" :
            self.state = state
        else:
            raise ValueError("Incorrect state")
        self.action = ""

    def __antelope (self) :
        if (self.state == "full") :
            self.action ="sleep"
            self.state = "hungry"
        else:
            self.action ="eat"
            self.state = "full"

    def __hunter (self) :
        if (self.state == "full") :
            self.action ="run"
            self.state = "hungry"
        else:
            self.action ="run"

    def __tree (self) :
        if (self.state == "full") :
            self.action ="look"
            self.state = "hungry"
        else:
            self.action ="sleep"

    def implementation (self, object) :
        if object == "antelope" :
            self.__antelope()
        elif object ==  "hunter" :
            self.__hunter()
        elif object == "tree" :
            self.__tree()
        else :
            raise ValueError("Incorrect object")
