class Shape:
    class Square:
        def __init__(self, length):
            self.AREA = length ** 2
        def area(self, num = 0):
            print("area =", num)

    def area(self, num = 0):
            print("area =", num)

length = int(input())
fig = Shape.Square(length)
fig.area(fig.AREA)