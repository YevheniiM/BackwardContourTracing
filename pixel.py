class Pixel:
    """
    A class that represents a pixel of the photo.

    """
    neighbors = {
        0: (-1, -1), 1: (0, -1), 2: (1, -1), 3: (1, 0),
        4: (1, 1), 5: (0, 1), 6: (-1, 1), 7: (-1, 0)
    }

    def __init__(self, x, y, value):
        """
        Class constructor.

        :param x: int
        :param y: int
        :param value: int

        """
        self.value = value
        self.x = x
        self.y = y
        self.marked = False

    def __str__(self):
        """
        A function that is intended to represent the pixel class for a user.

        :return: string

        """
        return "({0}, {1})".format(
            self.x, self.y
        )

    def __repr__(self):
        """
        A function that is intended to represent the Pixel class for a
        programmer.

        :return: string

        """
        return str(self.value) + str(self.marked)

    def __eq__(self, other):
        """
        A function that is intended to compare two pixels.

        :param other: Pixel
        :return: bool

        """
        if not isinstance(other, Pixel):
            return False

        return self.y == other.y and self.x == other.x
