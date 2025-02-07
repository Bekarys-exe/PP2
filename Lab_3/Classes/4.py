import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, secPoint):
        return math.sqrt((self.x - secPoint.x)**2 + (self.y - secPoint.y)**2)

x, y = map(int, input("Enter your x and y(example:5 3): ").split())
point1 = Point(x, y)
x, y = map(int, input("Enter your x and y(example:5 3): ").split())
point2 = Point(x, y)
point1.show()
point2.show()
x, y = map(int, input("Enter your x and y(example:5 3): ").split())
point1.move(x, y)
point1.show()
print(f"Distance between points: {point1.dist(point2)}")