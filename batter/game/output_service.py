import sys
from game import constants
from asciimatics.widgets import Frame
from game.handle_collisions_action import HandleCollisionsAction
from time import sleep

class OutputService:

    def __init__(self, screen):
        self._screen = screen
        self._collision = HandleCollisionsAction
        
    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering.""" 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)
        
    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.
        """ 
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, 7) # WHITE

    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        """Renders the screen.""" 
        self._screen.refresh()

    def delete_brick(self, brick):
        x = brick.get_x()
        y = brick.get_y()
        self._screen.clear_buffer(7, 0, 0, x, y, 0, 0)


    def game_over(self, screen):
        self._screen.clear_buffer(7, 0, 0)
        middle_x = int(constants.MAX_X / 2)
        middle_y = int(constants.MAX_Y / 2)
        screen.print_at('Game Over', middle_x, middle_y)
        screen.refresh()
        sleep(5)

    def game_over_start(self):
        self._screen.wrapper(self.game_over)
        quit()

    def win(self, screen):
        self._screen.clear_buffer(7, 0, 0)
        middle_x = int(constants.MAX_X / 2)
        middle_y = int(constants.MAX_Y / 2)
        screen.print_at('You win', middle_x, middle_y)
        screen.refresh()
        sleep(5)

    def game_win(self):
        self._screen.wrapper(self.win)
        quit()
        

        
