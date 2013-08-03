import curses


class View(object):
    def __init__(self, x, y, width, height):
        #draw border
        w = curses.newwin(height, width, y, x)
        w.box()
        w.refresh()

        #determine usable window dimensions
        self.width = width - 2
        self.height = height - 2
        self.max_x = self.width - 2
        self.max_y = self.height - 1

        #make window inside the border
        self.window = w.derwin(self.height, self.width, 1, 1)
        self.window.addstr(0, 0, '1')
        self.window.addstr(self.max_y, self.max_x, 'x')
        self.window.refresh()


class MainView(View):
    SCALE_MULTIPLIER = 2

    def __init__(self, x, y, width, height, system=0, scale=100):
        View.__init__(self, x, y, width, height)
        self.system = system
        self._scale = scale
        self.selection = 0

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
        self.redraw()

    def increase_scale(self, modifier=SCALE_MULTIPLIER):
        self.scale = self.scale * modifier

    def decrease_scale(self, modifier=SCALE_MULTIPLIER):
        self.scale = self.scale / modifier

    def display(self):
        for i in self.system.objects:
            y, x = int(round(i.y / self.scale)), int(round(i.x / self.scale))
            if y < self.height and y >= 0 and x < self.width and x >= 0:
                self.window.addstr(y, x, 'o')
        self.highlight()
        self.window.refresh()

    def selection_up(self):
        if self.selection > 0:
            self.selection -= 1
        else:
            self.selection = len(self.system.objects) - 1
        self.display()

    def selection_down(self):
        if self.selection < len(self.system.objects) - 1:
            self.selection += 1
        else:
            self.selection = 0
        self.display()

    def highlight(self):
        o = self.system.objects[self.selection]
        y, x = int(round(o.y / self.scale)), int(round(o.x / self.scale))
        if y < self.height and x < self.width:
            self.window.addstr(y, x, 'o', curses.A_STANDOUT)

    def redraw(self):
        self.window.clear()
        self.display()


class OverView(View):
    def __init__(self, x, y, width, height, system=0):
        View.__init__(self, x, y, width, height)
        self.system = system
        self.selection = 0

    def display(self):
        line = 0
        for i in self.system.objects:
            self.window.addstr(line, 0, '{0}:{1},{2}'.format(i.name, i.x, i.y))
            line += 1
        self.highlight()
        self.window.refresh()

    def selection_up(self):
        if self.selection > 0:
            self.selection -= 1
        else:
            self.selection = len(self.system.objects) - 1
        self.display()

    def selection_down(self):
        if self.selection < len(self.system.objects) - 1:
            self.selection += 1
        else:
            self.selection = 0
        self.display()

    def highlight(self):
        l = 0 + self.selection
        o = self.system.objects[self.selection]
        self.window.addstr(l, 0, '{0}:{1},{2}'.format(o.name, o.x, o.y), curses.A_STANDOUT)
