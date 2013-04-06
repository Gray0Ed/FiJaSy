import curses
import curses.textpad
import time
import atexit
import sys
import settings


def init_everything():
    """Call it before main loop."""
    global terminal_game
    terminal_game.init_systems()


def get_user_input():
    """Returns list of characters typed by player."""
    chars = []
    while "Elvis Lives":
        c = terminal_game.stdscr.getch()
        if c == -1:
            break
        chars += [c]
    return chars


def update_display(game):
    """Call this function draw current game state into terminal."""
    raise NotImplementedError


class TerminalDisplay:
    BEGIN_X = 0
    BEGIN_Y = 0

    def __init__(self, width=settings.DISPLAY_WIDTH, height=settings.DISPLAY_HEIGHT):
        self.width = width
        self.height = height

    def init_systems(self):
        self.stdscr = curses.initscr()
        curses.noecho()  # turn off automatic echoing of pressed keys
        self.stdscr.keypad(1)  # handle special keys
        curses.cbreak()  # react to pressed keys instantly without waiting for enter
        curses.curs_set(0)  # cursor will be invisible
        self.stdscr.nodelay(1)  # non blocking getch
        self.win = curses.newwin(self.height, self.width, self.BEGIN_Y, self.BEGIN_X)
        self.closed = False

        def exit_func():
            self.tear_down_systems()

        atexit.register(exit_func)

    def tear_down_systems(self):
        if self.closed:
            return
        self.closed = True
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def draw_game(self, game):
        #all_background = settings.DEFAULT_BACKGROUND_COLOR
        if game.player_typing_error:
            pass


terminal_game = TerminalDisplay()


x = 0
y = 0


def player_control(chars, tg):
    global x, y
    for c in chars:
        if c == ord('q'):
            return True  # Exit the while()
        elif c == curses.KEY_HOME:
            x = y = 0
        elif c == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif c == curses.KEY_RIGHT:
            x = min(tg.width - 1, x + 1)
        elif c == curses.KEY_UP:
            y = max(0, y - 1)
        elif c == curses.KEY_DOWN:
            y = min(tg.height, y + 1)
    return False


while True:
    tg = TerminalDisplay()
    tg.init_systems()

    print >> sys.stderr, curses.can_change_color()

    chars = []
    while "Elvis Lives":
        c = tg.stdscr.getch()
        if c == -1:
            break
        chars += [c]
    if player_control(chars, tg):
        break

    tg.stdscr.noutrefresh()
    tg.stdscr.clear()
    tg.stdscr.addstr(y, x, "hello world".encode('utf_8'))
    tg.stdscr.refresh()

    time.sleep(0.05)
