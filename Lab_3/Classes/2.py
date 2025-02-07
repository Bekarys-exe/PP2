class Shape:
    def __init__(self, area = 0):
        self.area = area
    def printArea(self):
        print(f"Area of the shape: {self.area}")

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area = self.length * self.length
    def printArea(self):
        print(f"Area of the square: {self.area}")

square = Square(int(input("Enter your length: ")))
square.printArea()
shape = Shape()
shape.printArea()
ex = input("Press ENTER to exit")