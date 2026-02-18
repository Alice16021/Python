import curses
import locale
import time
locale.setlocale(locale.LC_ALL, '')

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)

    y, x = 20, 20
    direction = (0, 1)
    while True:
        key = screen.getch()
        if key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_UP:
            y -= 1
        elif key in (0x1b, ord("q")): # <ESC>
            break
        screen.addstr(y, x, b"*")
        screen.refresh()
        time.sleep(0.1)


curses.wrapper(main)
