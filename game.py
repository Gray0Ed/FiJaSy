WORD_UNMATCHED = -2
WORD_OK = -1

class Game:
    def __init__(self, h, w, dictionary):
        self.height = h
        self.width = w 
        self.board = {}
        self.board[0] = [[False] * w] * h
        self.board[1] = [[False] * w] * h
        self.currentWord = {}
        self.currentWord[0] = ""
        self.currentWord[1] = ""
        self.dictionary = dictionary
        self.highlight = { 0 : [], 1 : []}
        self.HP = {0 : 0, 1 : 0}

    def singleMove(self):
        for row in range(0, h):
            for i in range(0,2):
                #player got hit
                if self.board[i][row][ (w - 1) * (1 - i)]:
                    HP[1 - i] -= 1;
            #TODO game finishing

            for column in range(w , 1, -1):
                self.board[0][row][column] = self.board[0][row][column - 1]
            for column in range(0, w - 1):
                self.board[1][row][column] = self.board[0][row][column + 1]
        
        explosions = []

        for row in range(0,h):
            for column in range(0, w):
                if board[0][row][column] and board[1][row][column]:
                    board[0][row][column] = False
                    board[1][row][column] = False
                    explosions.append( (row, column) )

                if (column < w - 1):
                    for i in range(0, 2):
                        if board[i][row][column] and board[1-i][row][column + 1]:
                            board[i][row][column] = False
                            board[1-i][row][column] = False
                            explosions.append( (row, column) )
        
        return explosions
       
    def charPress(self, player, character):
        self.currentWord[player] += character
        pref = self.currentWord[player]
        tmp_high = []
        for row in range(0,h):
            if (self.dictionary[row].startswith(pref)):
                if (self.dictionary[row] == pref):
                    self.highlight[player] = []
                    self.board[player][row][0] = True
                    return row
                else:
                    tmp_high.append(row)
        
        if (len(tmp_high) == 0):
            return WORD_UNMATCHED
        else:
            self.highlight[player] = tmp_high
            return WORD_OK
    

if __name__ == "__main__":
    x = Game(10,10)

