"""
Class Square that inherits from Rectangle
Base super class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor for square """
        super().__init__(size, size, x, y, id)
        self.size = self.width

    def __str__(self):
        """ __str__ method update """
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))
