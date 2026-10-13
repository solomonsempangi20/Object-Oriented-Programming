class Tail:
    def wag(self):
        print("Wag wag")

class Dog:
    def __init__(self, name):
        self.name = name
        self.tail = Tail()

    def greet(self):
        print("Woof woof, Happy to see you")
        self.tail.wag()
