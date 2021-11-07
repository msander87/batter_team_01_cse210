from game import constants
from game.point import Point

class MoveActorsAction():
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    Attributes:
        _count_ball (int): The number of frames since the ball moved.
        _former_ball_velocity (Point): The velocity of the ball before I stopped it.
    """
    def __init__(self):
        self._count_ball = 0
        self._former_ball_velocity = Point(0, 0)

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_text() == '*':
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """
        # The ball moves every other frame
        
        position = actor.get_position()
        velocity = actor.get_velocity()

        # Check if the ball can move
        if actor.get_text() == '@':
            velocity = self._check_if_ball_moved(velocity, constants.SLOWNESS_INDEX)

        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)

        # If paddle reached the edge of the screen, don't move
        if actor.get_text() == ('=' * constants.PADDLE_WIDTH):
            if (x1 == constants.MAX_X - constants.PADDLE_WIDTH
            and x2 > 0):
                x = constants.MAX_X - constants.PADDLE_WIDTH
            # elif (x1 == 0 and x2 < 0):
            #     x = 0
            
        position = Point(x, y)
        actor.set_position(position)

    def _check_if_ball_moved(self, ball_velocity, slowness_index):
        """Checks if the ball has moved.
        Args:
            ball (Actor): The ball to check.
            slowness_index (int): The index of the slowness to use.
        """
        if ball_velocity.get_x() != 0 and ball_velocity.get_y() != 0:
            self._former_ball_velocity = ball_velocity

        if self._count_ball == slowness_index:
            self._count_ball = 0
        else:
            self._count_ball += 1
            ball_velocity = Point(0, 0)

        return ball_velocity