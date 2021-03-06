'''1. Create a SquareGeometry class which takes in length as initialize parameter.
Make two methods getArea and getPerimeter inside this class.
Which when invoked returns area and perimeter of each square instance.'''

class SquareGeometry:
    def __init__(self, length):
        self.length = length

    def getArea(self):
        return self.length*self.length

    def getPerimeter(self):
        return 4*self.length


s1 = SquareGeometry(4)

print(s1.getArea())
print(s1.getPerimeter())
