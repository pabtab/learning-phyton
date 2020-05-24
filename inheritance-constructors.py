class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
point1.draw()

#excercise

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print('Talk with: ', self.name)


someone = Person('Pabtab')
someone.talk()


#inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()
