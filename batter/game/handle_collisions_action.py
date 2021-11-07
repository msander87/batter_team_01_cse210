import random
#from game.output_service import OutputService
from game import constants
from game.action import Action
from game.move_actors_action import MoveActorsAction
#from game.actor import Actor
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects 
    is to update the game state when actor collides.
    
    Stereotype:
        Controller
    """

    def __init__(self, output_service):

        self._output_service = output_service
        self.move = MoveActorsAction
        self.count_bricks = 0
        self.turn = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle= cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        ball = cast["ball"] [0] # there's only one

        

        #Check if the ball is bouncing against any of the 4 walls:
        
            #right wall
        if ball.get_position().get_x() == (constants.MAX_X -1):
            x = ball.get_velocity().get_x() * -1
            y = ball.get_velocity().get_y() 
            ball.set_velocity(Point(x, y))
            #left wall
        if ball.get_position().get_x() == 1:
            x = ball.get_velocity().get_x() * -1
            y = ball.get_velocity().get_y() 
            ball.set_velocity(Point(x, y))
            #top wall
        if ball.get_position().get_y() == 1:
            x = ball.get_velocity().get_x()
            y = ball.get_velocity().get_y() * -1
            ball.set_velocity(Point(x, y))
            #bottom wall
        if ball.get_position().get_y() == (constants.MAX_Y-1):
            self._output_service.game_over_start()
#----------------------------------------------------------------------------------
        ##Check if there is the ball collides with any of brick
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                x = ball.get_velocity().get_x()
                y = ball.get_velocity().get_y() 
                text = brick.get_text()
                if text != "" and x == 1 and y == -1:
                    brick.set_text("")
                    ball.set_velocity(Point(1, 1))
                    self.count_bricks += 1
                    break
                elif text != "" and x == -1 and y == -1:
                    brick.set_text("")
                    ball.set_velocity(Point(-1, 1))
                    self.count_bricks += 1
                    break
                elif text != "" and x == -1 and y == 1:
                    brick.set_text("")
                    ball.set_velocity(Point(-1, -1))
                    self.count_bricks += 1
                    break
                elif text != "" and x == 1 and y == 1:
                    brick.set_text("")
                    ball.set_velocity(Point(1, -1))
                    self.count_bricks += 1
                    break
                if self.count_bricks >= len(bricks):
                    self._output_service.game_win()

        # Point(1, -1) # upright
        # Point(-1, 1) # down left
        # Point(-1, -1) # up left
        # Point(1, 1) # donw right
#----------------------------------------------------------------------------------
        
        #Detect collisions between the ball and the paddles
        ball_x = ball.get_position().get_x()
        ball_y = ball.get_position().get_y()
        paddle_x = paddle.get_position().get_x()
        paddle_y = paddle.get_position().get_y()
        x_new = ball_x
        if ball_y == (paddle_y -1):
            if ball_x >= paddle_x -1 and ball_x <= (paddle_x + 11):
                x = ball.get_velocity().get_x()
                y = ball.get_velocity().get_y() * -1
                if x == 1 and ball_x < constants.MAX_X -2:
                    x_new = int(ball_x) + 1
                                   
                ball.set_velocity(Point(x, y))
                ball.set_position(Point(x_new, ball_y)) 


                #changing the direction of the ball based on where the ball hits the paddle
                #To make sure there is no set path for the ball

#optional code that needs a little more work 
'''
                #left edge of the paddle
                if ball_x >= (paddle_x) and ball_x <= (paddle_x + 2):
                    x = round(ball.get_velocity().get_x()* 1.5) 
                    y = round(ball.get_velocity().get_y()) 
                    ball.set_velocity(Point(x, y))
                #right edge of the paddle
                if ball_x >= (paddle_x + 8) and ball_x <= (paddle_x + 10):
                    x = round(ball.get_velocity().get_x()* 1.5) 
                    y = round(ball.get_velocity().get_y()) 
                    ball.set_velocity(Point(x, y))
                #middle of the paddle
                if ball_x >= (paddle_x + 3) and ball_x <= (paddle_x + 7):
                    x = round(ball.get_velocity().get_x()* .6) 
                    y = round(ball.get_velocity().get_y()) 
                    ball.set_velocity(Point(x, y))
'''