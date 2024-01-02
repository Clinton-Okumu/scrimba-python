class Person:
    def move(self):
        print("Moves 4 places")
    def rest(self):
        print("Gains 4 health points")
class Doctor(Person):
    def heal(self):
        print("Heal 10 health points")

class fighter:
    def heal(self):
        print("Do 10 points of health points")

character1 = Person()
character1.move()