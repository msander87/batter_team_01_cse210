class DrawActorsAction():
    """A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller
    Attributes:
        _output_service (OutputService): An instance of OutputService.
        counter (Counter): An instance of Counter.
        current_score (int): The current score.
        current_lives (int): The current lives.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self.__current_score = 0
        self.__current_lives = 5

    def set_score_and_lives(self, score, lives):
        """Sets the current score.
        Args:
            self: The current instance of DrawActorsAction.
        """
        self.__current_score = score
        self.__current_lives = lives

    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        
        for group in cast.values():
            self._output_service.draw_actors(group)

        #self._output_service.print_score_and_lives(self.__current_score, self.__current_lives)
        self._output_service.flush_buffer()