class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __del__(self):
        print("Point deleted")
    def output(self):
        print("OUTPUT X AND Y COORDINATES OF A POINT")
        print("x = " + str(self.x) + "; y = " + str(self.y))

A = Point()
A.output()
B = Point(3.2, 5.4)
B.output()
# Can delete even if it's not a pointer
# del A
# del B
C = Point(5.4)
C.output()
