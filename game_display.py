import curses
import curses.textpad
import time
import atexit
import sys
import settings


class Displayable(object):
    BULLET_STATE_NORMAL = 0
    BULLET_STATE_EXPLODED = 1

    def our_bullets(self):
        """Returns list of triples (y, x, state) representing
           positions and states of bullets shoted by local player."""
        raise NotImplementedError

    def enemy_bullets(self):
        """Returns list of triples (y, x, state) representing
           positions and states of bullets shoted by enemy player."""
        raise NotImplementedError

    def words_to_type(self):
        """Returns list of pairs (word, letters_typed) where
        letters_typed is number of letters of given word which are
        already typed"""
        raise NotImplementedError

    def our_hp(self):
        """Returns number representing player HP."""
        raise NotImplementedError

    def enemy_hp(self):
        """Returns number representing enemy HP."""
        raise NotImplementedError

    def local_player_hitted(self):
        """Returns list of lines where player was hit"""
        raise NotImplementedError

    def enemy_player_hitted(self):
        """Returns list of lines where enemy player was hit."""
        raise NotImplementedError
    
    def recent_explosions(self):
        """Returns list of explosions"""

        raise NotImplementedError

    def typing_error(self):
        """Returns True if player did recently typing error."""
        return False

    def enemy_typed_sth(self):
        """Returns wumber of line where enemy typed something.
        -1 if enemy does not type anything in last frame.
        """
        return -1

    def debug(self):
        """Returns string with debug information."""
        return ""

    def our_CPS(self):
        return 0

    def enemy_CPS(self):
        return 0

    def our_typo_rate(self):
        return 0

    def enemy_typo_rate(self):
        return 0


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
        curses.start_color()
        self.init_color_pairs()

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

    def init_color_pairs(self):
        counter = 0
        self.color_pairs_map = {}
        for fg in xrange(8):
            for bg in xrange(8):
                curses.init_color(counter, fg, bg)
                self.color_pairs_map[(fg, bg)] = counter
                counter += 1

    def draw_string_with_colors(self, s, y, x, fg, bg):
        self.stdscr.addstr(y, x, s.encode('utf_8'), self.color_pairs_map[(fg, bg)])

    def tear_down_systems(self):
        if self.closed:
            return
        self.closed = True
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def draw_game(self, game):
        all_background = settings.DEFAULT_BACKGROUND_COLOR
        words_background = settings.DEFAULT_BACKGROUND_COLOR

        if player_typing_error:
            words_background = settings.TYPO_FLASH_COLOR
        if player_hitted_recently:
            all_background = settings.AFTER_DAMAGE_BACKGROUND_COLOR


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


init_everything()

for i in xrange(64):
    print >> sys.stderr, curses.pair_content(i)


while True:
    chars = []
    chars = get_user_input()
    if player_control(chars, terminal_game):
        break

    terminal_game.stdscr.noutrefresh()
    terminal_game.stdscr.clear()
    terminal_game.stdscr.addstr(y, x, "hello world".encode('utf_8'))
    terminal_game.stdscr.refresh()

    time.sleep(0.05)
