class AocError(Exception):
    """ base exception for aoc package """

class UserNotFoundError(Exception):
    """ user session id was not found """

class PuzzleNotStartedError(Exception):
    """ puzzle has not started yet """