class Animal:
    def __init__(self, name):
        self.name = name

    def sound1(self):
        print(self.name + '在水上游泳')


class Dog:
    def __init__(self, name):
        self.p =name

    def sound(self):
        return '汪汪叫'

    def move(self):
        print(self.p + '在馬路上行走')


d = Dog('小黑')
print(d.p, d.sound())
d.move()
d.sound()