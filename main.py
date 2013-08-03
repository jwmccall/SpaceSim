import curses
import space
import view


def run(stdscr):
    curses.curs_set(0)

    max_y, max_x = stdscr.getmaxyx()
    stdscr.refresh()

    overview_width = 30
    main_view = view.MainView(0, 0, max_x - overview_width, max_y)
    overview = view.OverView(max_x - overview_width, 0, overview_width, max_y)

    #status window
    #statuswin = curses.newwin(5, max_x, max_y - 5, 0)
    #statuswin.border(0, 0, 0, 0, curses.ACS_LTEE, curses.ACS_RTEE, 0, 0)
    #statuswin.refresh()

    s = space.System()
    s.objects.append(space.Celestial(x=100, y=275))
    s.objects.append(space.Celestial(x=200, y=500))
    s.objects.append(space.Celestial(x=20000, y=1700))
    s.objects.append(space.Celestial(x=5400, y=2500))
    main_view.system = s
    overview.system = s
    main_view.display()
    overview.display()

    #main loop
    while 1:
        c = stdscr.getch()
        main_view.window.refresh()
        overview.window.refresh()
        if c == ord('q'):
            break
        elif c == curses.KEY_UP:
            overview.selection_up()
            main_view.selection_up()
        elif c == curses.KEY_DOWN:
            overview.selection_down()
            main_view.selection_down()
        elif c == ord('+'):
            main_view.decrease_scale()
        elif c == ord('-'):
            main_view.increase_scale()
        elif c == curses.KEY_RESIZE:
            pass

if __name__ == "__main__":
    curses.wrapper(run)
