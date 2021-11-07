class Counter:
    """Keeps track of the number of score and lives the player has
    
    Stereotype:
        Information Holder
    Attributes:
        __score (int): the number of points the player has
    Methods: 
        increment(), decrement(), reset(), get_points()
    """
    def __init__(self):
        """The class contructor
        Args: 
            Self: An instance of Counter
        """
        self.__score = 0
        self.__lives = 5

    def increment(self):
        """Increments the score by 1
        Args: 
            self: An instance of Counter
            score (int): the number of points to increment by
        """
        self.__score += 1

    def decrement(self):
        """Decrements the score by 1
        Args: 
            self: An instance of Counter
            score (int): the number of points to increment by
        """
        self.__score -= 1

    def decrement_lives(self):
        """Decrements the number of lives the player has
        by 1
        Args: 
            self: An instance of Counter
        """
        self.__lives -= 1

    def reset(self):
        """Resets the score to 0
        Args: 
            self: An instance of Counter
        """
        self.__score = 0

    def get_lives(self):
        """Get the number of lives the player has
        Args: 
            self: An instance of Counter
        """
        return self.__lives

    def get_score(self):
        """Gets the score the player has
        Arg:
            self: An instance of Counter
        """
        return self.__score