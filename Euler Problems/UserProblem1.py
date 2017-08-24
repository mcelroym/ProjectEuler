import math

class Square:
    center = 0
    vertex1 = 0
    vertex2 = 0
    vertex3 = 0
    vertex4 = 0
    area = 0

    def __init__(self, center, vertex):
        self.area = 2 * self.EuclideanDistance(center, vertex) ** 2
        self.vertex1 = vertex

        #find vertex2, vertex3, vertex4

    def EuclideanDistance(self, x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

    def OverlappingArea(self, square):
        pass

    def Intersections(self, square):
        pass



test = Square([0,0],[1,1])
print test.area