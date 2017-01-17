import point3D as pt3D


class Triangle3D(object):
    def __init__(self, ID=0, point1=None, point2=None, point3=None):
        self.id = ID
        self.point1 = point1 or pt3D.Point3D()  # (0,0,0) by default
        self.point2 = point2 or pt3D.Point3D()  # (0,0,0) by default
        self.point2 = point2 or pt3D.Point3D()  # (0,0,0) by default

    def printEl(self):
        print("id : " + str(self.id))
        print("point 1")
        self.point1.printEl()
        print("point 2")
        self.point1.printEl()
        print("point 3")
        self.point1.printEl()
