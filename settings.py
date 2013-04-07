"""
board example
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                                                                                                        X
     Your HP: 18                                                                              Enemy HP: 22              X
          CPS: 4.11                                                                                 CPS: 5.8            X
          typo raito: 0.01                                                                          typo raito: 0.0     X
________________________________________________________________________________________________________________________X
               star||                                                                                            ||     X
              candy||                                                                                            ||     X
              wings||                                                                                            ||     X
        salutations||                                                                                            ||     X
              power||                                                                                            ||     X
             string||                                                                                            ||     X
         carburetor||                                                                                            ||     X
           shopping||                                                                                            ||     X
              blond||                                                                                            ||     X
              steak||                                                                                            ||     X
           speakers||                                                                                            ||     X
            grimace||                                                                                            ||     X
               case||                                                                                            ||     X
           stubborn||                                                                                            ||     X
              couch||                                                                                            ||     X
       announcement||                                                                                            ||     X
                cat||                                                                                            ||     X
           elevator||                                                                                            ||     X
             marker||                                                                                            ||     X
              swish||                                                                                            ||     X
           gangrene||                                                                                            ||     X
         scurrilous||                                                                                            ||     X
             photon||                                                                                            ||     X
              cabal||                                                                                            ||     X
            stentor||                                                                                            ||     X
           youngish||                                                                                            ||     X
              swish||                                                                                            ||     X
              elver||                                                                                            ||     X
            organza||                                                                                            ||     X
            febrile||                                                                                            ||     X
------------------------------------------------------------------------------------------------------------------------X
                                                                                                                        X
                    DEBUG                                                                                               X
                                                                                                                        X
                                                                                                                        X
                                                                                                                        X
                                                                                                                        X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
"""
import curses

DEFAULT_BACKGROUND_COLOR = curses.COLOR_BLACK
TYPO_FLASH_COLOR = curses.COLOR_RED
OUR_BULLETS_COLOR = curses.COLOR_WHITE
ENEMY_BULLETS_COLOR = curses.COLOR_WHITE
AFTER_DAMAGE_BACKGROUND_COLOR = curses.COLOR_MAGENTA
TEXT_COLOR = curses.COLOR_WHITE
TYPED_TEXT_COLOR = curses.COLOR_YELLOW
INFO_BAR_BACKGROUND = curses.COLOR_BLACK


MAX_WORD_LEN = 18
PERIODICITY = 5
NUMBER_OF_BATTLE_ROWS = 30
NUMBER_OF_BATTLE_COLUMNS = 100
BATTLE_START_X = MAX_WORD_LEN + 2

DISPLAY_WIDTH = 120
DISPLAY_HEIGHT = 50
PLAYERS_INFO_Y = 2
BATTLE_START_Y = PLAYERS_INFO_Y + 4
PLAYERS_INFO_MARGIN = 4
PLYAERS_MAX_HP = 10
TYPO_RATE_NUMBER_LEN = 4
CPS_NUMBER_LEN = 4

OUR_BULLET_CHAR = '>'
ENEMY_BULLET_CHAR = '<'
BULLET_EXPL_BACKGROUND = curses.COLOR_YELLOW
BULLET_EXPL_CHAR_COLOR = curses.COLOR_RED
BULLET_EXPL_CHAR = 'O'

DICTIONARY = [
    'star', 'candy', 'wings', 'salutations',
    'power', 'string', 'carburetor', 'shopping',
    'blond', 'steak', 'speakers', 'grimace', 'case',
    'stubborn', 'couch', 'announcement', 'cat', 'elevator',
    'marker', 'swish', 'gangrene', 'scurrilous', 'photon'
    'cabal', 'stentor', 'youngish', 'swish', 'elver',
    'organza', 'febrile', 'lolol'
]

assert len(DICTIONARY) == NUMBER_OF_BATTLE_ROWS
