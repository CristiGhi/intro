# Creati o clasa Rectangle, care are 2 atribute width si length, instantiate in cadrul constructorului cu 2 valori integer.
# a) Pentru clasa respectiva creati o functie get_area care returneaza aria dreptunghiului.
# b) Creati si o functie display care afiseaza dreptunghiul folosind un parametru optional pentru a desena, in cazul in care
# parametrul nu este dat, se foloseste ca default caracterul *.
# Exemplu de rulare:
# new_rectangle = Rectange(2, 4)
# print(new_rectangle.get_area()) => 8
# new_rectangle.display() => ****     sau: new_rectangle('#') => ####
#                            ****                                ####
class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def get_area(self):
        return self.width * self.lenght

    def display(self, character = '*'):
        for i in range(self.width):
            print(self.lenght * character)

new_rectangle = Rectangle(2, 4)
print(new_rectangle.get_area())
new_rectangle.display()
