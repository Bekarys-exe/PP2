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

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.area = self.length * self.width
    def printArea(self):
        print(f"Area of the square: {self.area}")

length, width = map(int, input("Enter your length and width(example:5 3): ").split())
rectangle = Rectangle(length, width)
rectangle.printArea()
shape = Shape()
shape.printArea()
ex = input("Press ENTER to exit")