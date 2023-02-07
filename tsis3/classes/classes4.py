class Points:
    def __init__(self, px = 0, py = 0):
        self.x = px
        self.y = py
    def show(self):
        print(self.x, self.y)

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = dx**2 + dy**2
        distance = distance ** 0.5
        print(distance)

x1, y1 = input().split()
x2, y2 = input().split()
x1, y1 = int(x1), int(y1)
x2, y2 = int(x2), int(y2)

point1 = Points(x1, y1)
point2 = Points(x2, y2)

point1.show()
point2.show()

point1.move(1, 1)
point2.move(2, 2)

point1.show()
point2.show()

point1.dist(point2)