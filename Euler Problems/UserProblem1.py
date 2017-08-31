import math

class Square:
    center = [0, 0]
    vertex = [[0,0], [0,0], [0,0], [0,0]]
    area = [0, 0]

    def __init__(self, center, vert):
        self.area = 2 * self.EuclideanDistance(center, vert) ** 2


        vec = [center[0] - vert[0], center[1] - vert[1]]
        norm = [vert[1] - center[1], center[0] - vert[0]]

        # Get all the vertices of our square
        self.vertex[0] = vert
        self.vertex[1] = [center[0] + norm[0], center[1] + norm[1]]
        self.vertex[2] = [center[0] + vec[0], center[1] + vec[1]]
        self.vertex[3] = [center[0] - norm[0], center[1] +- norm[1]]

    def EuclideanDistance(self, x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

    def AreaOfPolygon(self, points):
        # Use Shoestring Algorithm
        A = 0

        for i in range(len(points) - 1):
            A += points[i][0] * points[i+1][1]
        A += points[len(points)-1][0] * points[0][1]

        for i in range(len(points) - 1):
            A -= points[i+1][0] * points[i][1]
        A -= points[0][0] * points[len(points)-1][1]

        A = abs(A)
        A /= 2

        return A


    def OverlappingPolygon(self, square):
        # Find a list of points at which two squares intersect
        pass


test = Square([0,0], [1,1])

