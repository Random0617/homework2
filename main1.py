class Point:
    x = 0
    y = 0
    def __init__(self):
        self.x = 3
        self.y = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def output(self):
        print("OUTPUT X AND Y COORDINATES OF A POINT")
        print("x = " + str(self.x) + "; y = " + str(self.y))

A = Point()
A.output()
B = Point(3.2, 5.4)
B.output()
