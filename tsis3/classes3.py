class Shape:
    class Square:
        def __init__(self, length):
            self.AREA = length ** 2
        def area(self, num = 0):
            print("area =", num)

    def area(self, num = 0):
            print("area =", num)

class Rectangle(Shape):
    def init(self, length, width):
        self.AREA = length * width
        self.area(self.AREA)


length, width = input().split()
length = int(length)
width = int(width)

rec = Rectangle()
rec.init(length, width)
