import game_display
import settings
import time
import curses
import curses.textpad

WORD_UNMATCHED = -2
WORD_OK = -1

class Game(game_display.Displayable):
    def __init__(self, w, dictionary):
        self.height = len(dictionary)
        self.width = w 
        self.board = {}
        self.board[0] = [[False for _ in range(w) ] for _ in range (self.height)]
        self.board[1] = [[False for _ in range(w) ] for _ in range (self.height)]
        self.currentWord = ""
        self.dictionary = dictionary
        self.highlight = [0] * self.height 
        self.HP = {0 : 0, 1 : 0}
        self.local_hits = []
        self.enemy_hits = []
        self.explosions = []
    
    def print_me(self, player):
        for i in range(self.height):
            print self.board[player][i]

    def singleMove(self):
        for row in range(0, self.height):
            if self.board[0][row][self.width - 1]:
                self.local_hits += [row]
                self.HP[1] -= 1
            if self.board[1][row][0]:
                self.enemy_hits += [row]
                self.HP[0] -= 1

            #TODO game finishing

            for column in range(self.width - 1 , 0, -1):
                self.board[0][row][column] = self.board[0][row][column - 1]

            for column in range(0, self.width - 1):
                self.board[1][row][column] = self.board[0][row][column + 1]
            
            self.board[0][row][0] = False
            self.board[1][row][ self.width - 1] = False

        for row in range(0, self.height):
            for column in range(0, self.width):
                if self.board[0][row][column] and self.board[1][row][column]:
                    self.board[0][row][column] = False
                    self.board[1][row][column] = False
                    self.explosions.append( (row, column) )

                if (column < self.width - 1):
                    for i in range(0, 2):
                        if self.board[i][row][column] and self.board[1-i][row][column + 1]:
                            self.board[i][row][column] = False
                            self.board[1-i][row][column] = False
                            self.explosions.append( (row, column) )
        
       
    def charPress(self, character):
        self.currentWord += character
        pref = self.currentWord
        tmp_high = [0] * self.height
        match_seeked = False;
        for row in range(0, self.height):
            if (self.dictionary[row].startswith(pref)):
                if (self.dictionary[row] == pref):
                    self.highlight = [0] * self.height
                    self.board[0][row][0] = True
                    return row
                else:
                    tmp_high[row] = 1
                    match_seeked = True;
        
        if not match_seeked:
            self.currentWord = self.currentWord[0 : -1]
            return WORD_UNMATCHED

        else:
            self.highlight = tmp_high
            return WORD_OK

    def our_bullets(self):
        res = []
        for row in range(0, self.height):
            for column in range(0, self.width):
                if (self.board[0][row][column]):
                    res.append((row, column, self.BULLET_STATE_NORMAL))
        
        return res

    def enemy_bullets(self):
        res = []
        for row in range(0, self.height):
            for column in range(0, self.width):
                if (self.board[1][row][column]):
                    res.append((row, column, self.BULLET_STATE_NORMAL))
        return res
    
    def words_to_type(self):
        res = []
        for i in range(0, self.height):
            res.append( (self.dictionary[i], self.highlight[i] * len(self.currentWord)))

        return res

    def our_hp(self):
        return self.HP[0]

    def enemy_hp(self):
        return self.HP[1]

    def local_player_hitted(self):
        tmp = self.enemy_hits;
        self.enemy_hits = []
        return tmp
    
    def enemy_player_hitted(self):
        tmp = self.local_hits
        self.local_hits = []
        return tmp

    def recent_explosions(self):
        tmp = self.explosions
        self.explosions = []
        return tmp


if __name__ == "__main__":
    game_display.init_everything()
    x = Game(100, settings.DICTIONARY)
    x.charPress('c')
    x.charPress('a')
    x.charPress('t')
    x.singleMove()
    game_display.update_display(x)

    try:
        while True:
            game_display.update_display(x)
            #terminal_game.draw_info_bar(DummyDisplayable())
            x.singleMove()
        # terminal_game.stdscr.noutrefresh()
        # terminal_game.stdscr.clear()
        # terminal_game.stdscr.addstr(y, x, "hello world".encode('utf_8'))
            game_display.terminal_game.stdscr.refresh()

            time.sleep(0.05)
    finally:
        game_display.terminal_game.tear_down_systems()

