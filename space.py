import random


class Celestial(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.name = 'C{0}'.format(random.randint(1111, 9999))


class Star(Celestial):
    pass


class System(Celestial):
    def __init__(self):
        self.star = Star(0, 0)
        self.objects = []


class Sector(object):
    WIDTH = 6
    HEIGHT = 6

    def __init__(self):
        self.grid = [[None] * Sector.WIDTH for __ in range(Sector.HEIGHT)]
        self.grid[0][1] = '*'

if __name__ == '__main__':
    s = Sector()
    print s.grid
