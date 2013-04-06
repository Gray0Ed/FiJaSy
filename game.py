from game_display import Displayable

WORD_UNMATCHED = -2
WORD_OK = -1

class Game(Displayable):
    def __init__(self, h, w, dictionary):
        self.height = h
        self.width = w 
        self.board = {}
        self.board[0] = [[False] * w] * h
        self.board[1] = [[False] * w] * h
        self.currentWord = ""
        self.dictionary = dictionary
        self.highlight = [] * len(dictionary) 
        self.HP = {0 : 0, 1 : 0}
        self.local_hits = []
        self.enemy_hits = []
        self.explosions = []

    def singleMove(self):
        for row in range(0, h):
            if self.board[0][row][w-1]:
                self.local_hits += [row]
                self.HP[1] -= 1
            if self.board[1][row][0]:
                self.enemy_hits += [row]
                self.HP[0] -= 1

            #TODO game finishing

            for column in range(w , 1, -1):
                self.board[0][row][column] = self.board[0][row][column - 1]
            for column in range(0, w - 1):
                self.board[1][row][column] = self.board[0][row][column + 1]
        
        for row in range(0,h):
            for column in range(0, w):
                if self.board[0][row][column] and self.board[1][row][column]:
                    self.board[0][row][column] = False
                    self.board[1][row][column] = False
                    self.explosions.append( (row, column) )

                if (column < w - 1):
                    for i in range(0, 2):
                        if self.board[i][row][column] and self.board[1-i][row][column + 1]:
                            self.board[i][row][column] = False
                            self.board[1-i][row][column] = False
                            self.explosions.append( (row, column) )
        
       
    def charPress(self, character):
        self.currentWord += character
        pref = self.currentWord
        tmp_high = [0] * len(dictionary)
        match_seeked = False;
        for row in range(0,h):
            if (self.dictionary[row].startswith(pref)):
                if (self.dictionary[row] == pref):
                    self.highlight = True
                    self.board[player][row][0] = True
                    return row
                else:
                    tmp_high[row] = True
                    match_seeked = True;
        
        if not match_seeked:
            self.currentWord = self.currentWord[0 : -1]
            return WORD_UNMATCHED

        else:
            self.highlight = tmp_high
            return WORD_OK

    def our_bullets(self):
        res = []
        for row in range(0, h):
            for column in range(0, w):
                if (self.board[0][row][column]):
                    res += [(row, column, BULLET_STATE_NORMAL)]
        
        return res

    def enemy_bullets(self):
        res = []
        for row in range(0, h):
            for column in range(0, w):
                if (self.board[1][row][column]):
                    res += [(row, column, BULLET_STATE_NORMAL)]
        return res
    
    def words_to_type(self):
        res = []
        for i in range(0,h):
            res += [ self.dictionary[i], self.highlight[i] * len(self.currentWord) ]

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
    x = Game(10,10)

