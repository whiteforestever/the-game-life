"""The main module for launching the game"""

import atexit
import pygame
from game_field import GameField
from os import sys


def __phrase_after_the_game():
        """The last phrase that says goodbye to the user"""
        print("Thank you for playing! Come back as soon as possible!")

if __name__ == "__main__":

    playing_field = GameField()
    visual_field = playing_field.create_field()
    atexit.register(__phrase_after_the_game)

    is_playing = 0
    while True:
        playing_field.draw_field_with_cells(visual_field)

        if is_playing:
            playing_field.update_field()

        # get all events from the queue
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (event.type == pygame.QUIT):
                """ESC key pressed or window close X pressed"""
                print("Exit from the game")
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                """Revive or kill the cage"""
                if event.button == 1:   # left mouse button
                    playing_field.cell_clicked(event.pos)    # The coordinates of the cursor when the mouse button is clicked are in 'event.pos'
                """Change mode: either life goes on, or time has stopped"""
                if event.button == 3:   # right mouse button
                    is_playing ^= 1    # Looks like magic, but it simply changes 1 -> 0 or 0 -> 1
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                """To produce only one generation"""
                playing_field.update_field()
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE):
                """To clean up the field"""
                playing_field.clean_field()
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_r):
                """To set up random field"""
                playing_field.set_random_field()

        pygame.display.update()