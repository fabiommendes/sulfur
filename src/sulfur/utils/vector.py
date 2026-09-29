import collections

_Shape = collections.namedtuple('Shape', ['width', 'height'])
_Position = collections.namedtuple('Position', ['x', 'y'])


class Position(_Position):
    """
    Represents screen positions.
    """

    def __add__(self, other):
        x, y = other
        return Position(x=self.x + x, y=self.y + y)

    def __sub__(self, other):
        x, y = other
        return self.__add__((-x, -y))


class Shape(_Shape):
    """
    Represents rectangular shapes with given width and height.
    """

    def rescale(self, scale):
        """
        Returns a copy rescaled by the given scale factor.
        """
        return Shape(scale * self.x, scale * self.y)