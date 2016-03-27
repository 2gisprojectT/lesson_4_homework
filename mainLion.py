class Lion :
    def __init__(self, x, y) :
        self.state = x
        self.action = ""
        self.read_and_go(y)

    def antelope (self) :
        if (self.state == 1) :
            self.action ="sleep"
            self.state = 0
        else:
            self.action ="eat"
            self.state = 1

    def hunter (self) :
        if (self.state == 1) :
            self.action ="run"
            self.state = 0
        else:
            self.action ="run"

    def tree (self) :
        if (self.state == 1) :
            self.action ="look"
            self.state = 0
        else:
            self.action ="sleep"

    def other (self) :
        self.action = "error"

    def read_and_go (self, y) :
        word = y
        if word == "antelope" :
            self.antelope()
        elif word == "hunter" :
            self.hunter()
        elif word == "tree" :
            self.tree()
        else :
            self.other()