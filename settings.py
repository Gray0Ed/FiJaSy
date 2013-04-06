"""
board example
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
                                                                                                                        X
     Your HP: 18                                                                              Enemy HP: 22              X
          CPS: 4.11                                                                                 CPS: 5.8            X
          typo rate: 0.01                                                                           typo rate: 0.0      X
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
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾X
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
OUR_BULLETS_COLOR = curses.COLOR_CYAN
ENEMY_BULLETS_COLOR = curses.COLOR_BLUE
AFTER_DAMAGE_BACKGROUND_COLOR = curses.COLOR_MAGENTA

NUMBER_OF_BATTLE_ROWS = 30
NUMBER_OF_BATTLE_COLUMNS = 100

DISPLAY_WIDTH = 120
DISPLAY_HEIGHT = 50
ACTION_PADDING_TOP = 10
ACTION_PADDING_BOTTOM = 10
MAX_STRING_LEN = 20
DICTIONARY = {
        0 : 'candy',
        }
