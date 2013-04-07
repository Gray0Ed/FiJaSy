import curses
import curses.textpad
import time
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
    terminal_game.draw_game(game)


def restore_terminal_display():
    terminal_game.tear_down_systems()


class DummyDisplayable(Displayable):
    def words_to_type(self):
        a = map(lambda x: (x, 0), settings.DICTIONARY)
        a[0] = (settings.DICTIONARY[0], 2)
        return a

    def our_hp(self):
        return 18

    def enemy_hp(self):
        return 22

    def our_CPS(self):
        return 4.11

    def enemy_CPS(self):
        return 5.8

    def our_typo_rate(self):
        return 0.1

    def enemy_typo_rate(self):
        return 0.01

    def local_player_hitted(self):
        return []

    def typing_error(self):
        return False

    def recent_explosions(self):
        return [(0, 0), (5, 1)]

    def our_bullets(self):
        return [(0, 0, 0), (5, 0, 0), (20, 80, 0)]

    def enemy_bullets(self):
        return [(0, 1, 0), (5, 1, 0), (10, 90, 0)]


class TerminalDisplay:
    BEGIN_X = 0
    BEGIN_Y = 0

    def __init__(self, width=settings.DISPLAY_WIDTH, height=settings.DISPLAY_HEIGHT):
        self.width = width
        self.height = height
        self.HP_DIGITS = len(str(settings.PLYAERS_MAX_HP))

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

#        def exit_func():
#            self.tear_down_systems()

#        atexit.register(exit_func)

    def init_color_pairs(self):
        counter = 1
        self.color_pairs_map = {(0, 7): 0}
        for fg in xrange(8):
            for bg in xrange(8):
                if fg == 0 and bg == 7:
                    continue
                curses.init_pair(counter, fg, bg)
                self.color_pairs_map[(fg, bg)] = counter
                counter += 1

    def draw_string_with_colors(self, s, y, x, fg, bg):
        self.stdscr.addstr(y, x, s.encode('utf_8'), curses.color_pair(self.color_pairs_map[(fg, bg)]))
        return len(s)

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

        if game.local_player_hitted():
            all_background = settings.AFTER_DAMAGE_BACKGROUND_COLOR

        self.draw_info_bar(game)
        self.draw_words(game, all_background)
        self.draw_string_with_colors('-' * settings.DISPLAY_WIDTH,
                settings.NUMBER_OF_BATTLE_ROWS + settings.BATTLE_START_Y, 0,
                curses.COLOR_WHITE, all_background)
        self.draw_battle(game, all_background)

    def draw_battle(self, game, all_background):
        sby = settings.BATTLE_START_Y
        eby = settings.BATTLE_START_Y + settings.NUMBER_OF_BATTLE_ROWS
        sbx = settings.BATTLE_START_X
        ebx = settings.BATTLE_START_X + settings.NUMBER_OF_BATTLE_COLUMNS
        for y in xrange(sby, eby):
            self.draw_string_with_colors(" " * (ebx - sbx), y, sbx,
                    curses.COLOR_WHITE, all_background)
        explos = set(game.recent_explosions())

        bullets = (map(lambda x: (x, True), game.our_bullets()) +
                   map(lambda x: (x, False), game.enemy_bullets()))

        for (by, bx, _), ours in bullets:
            expl = False
            if (by, bx) in explos:
                expl = True
            by += settings.BATTLE_START_Y
            bx += settings.BATTLE_START_X

            if ours:
                bcolor = settings.OUR_BULLETS_COLOR
                char = settings.OUR_BULLET_CHAR
            else:
                bcolor = settings.ENEMY_BULLETS_COLOR
                char = settings.ENEMY_BULLET_CHAR

            bg = all_background

            if expl:
                bg = settings.BULLET_EXPL_BACKGROUND
                bcolor = settings.BULLET_EXPL_CHAR_COLOR
                char = settings.BULLET_EXPL_CHAR

            self.draw_string_with_colors(char, by, bx, bcolor, bg)

    def draw_words(self, game, bg):
        if game.typing_error():
            bg = settings.TYPO_FLASH_COLOR
        words_to_type = game.words_to_type()
        assert len(words_to_type) == settings.NUMBER_OF_BATTLE_ROWS
        for dy, (word, ntyped) in enumerate(words_to_type):
            y = settings.BATTLE_START_Y + dy
            x = 0
            x += self.draw_string_with_colors(
                    " " * (settings.MAX_WORD_LEN - len(word)),
                    y, 0, curses.COLOR_WHITE, bg)

            if ntyped:
                x += self.draw_string_with_colors(word[:ntyped], y, x,
                        settings.TYPED_TEXT_COLOR, bg)
            self.draw_string_with_colors(word[ntyped:] + '||', y, x,
                    settings.TEXT_COLOR, bg)

    def draw_info_bar(self, game):
        for y in xrange(settings.PLAYERS_INFO_Y):
            self.draw_string_with_colors(' ' * settings.DISPLAY_WIDTH, y, 0,
                            settings.TEXT_COLOR, settings.INFO_BAR_BACKGROUND)
        info_r11 = ((" " * settings.PLAYERS_INFO_MARGIN + "Your HP: %s")
                            % str(game.our_hp()))
        info_r13 = (("Enemy HP: %s" + " " * (settings.PLAYERS_INFO_MARGIN + 7))
                            % str(game.enemy_hp()))
        info_r12 = " " * (settings.DISPLAY_WIDTH - len(info_r11) - len(info_r13))
        self.draw_string_with_colors(info_r11 + info_r12 + info_r13,
                        settings.PLAYERS_INFO_Y, 0,
                        settings.TEXT_COLOR, settings.INFO_BAR_BACKGROUND)

        info_r21 = ((" " * (settings.PLAYERS_INFO_MARGIN + 5) + "CPS: %s")
                    % str(game.our_CPS()))
        info_r23 = ((" " * 6 + "CPS: %s" + " " * (settings.PLAYERS_INFO_MARGIN + 5))
                    % str(game.enemy_CPS()))
        info_r22 = " " * (settings.DISPLAY_WIDTH - len(info_r21) - len(info_r23))

        self.draw_string_with_colors(info_r21 + info_r22 + info_r23,
                        settings.PLAYERS_INFO_Y + 1, 0,
                        settings.TEXT_COLOR, settings.INFO_BAR_BACKGROUND)

        info_r31 = ((" " * (settings.PLAYERS_INFO_MARGIN + 5) + "typo raito: %s")
                    % game.our_typo_rate())
        info_r33 = ((" " * 6 + "typo raito: %s" + " " * settings.PLAYERS_INFO_MARGIN)
                    % str(game.enemy_typo_rate()))
        info_r32 = " " * (settings.DISPLAY_WIDTH - len(info_r31) - len(info_r33))
        self.draw_string_with_colors(info_r31 + info_r32 + info_r33,
                        settings.PLAYERS_INFO_Y + 2, 0,
                        settings.TEXT_COLOR, settings.INFO_BAR_BACKGROUND)
        self.draw_string_with_colors("_" * settings.DISPLAY_WIDTH,
                settings.PLAYERS_INFO_Y + 3, 0, settings.TEXT_COLOR,
                settings.INFO_BAR_BACKGROUND)

terminal_game = TerminalDisplay()


if __name__ == "__main__":
    init_everything()

    try:
        while True:
            chars = []
            chars = get_user_input()
            update_display(DummyDisplayable())
            #terminal_game.draw_info_bar(DummyDisplayable())

        # terminal_game.stdscr.noutrefresh()
        # terminal_game.stdscr.clear()
        # terminal_game.stdscr.addstr(y, x, "hello world".encode('utf_8'))
            terminal_game.stdscr.refresh()

            time.sleep(0.05)
    finally:
        terminal_game.tear_down_systems()
