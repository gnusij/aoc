import sys
from .get import get_data_today
from .get import get_ex_today
from .get import get_data
from .get import get_ex

from .version import __version__


__all__ = [
    "data",
    "lines",
    "ex",
    "get",
    "get_ex",
]

class Aoc(object):
    _module = sys.modules[__name__]

    def __dir__(self):
        return __all__

    def __getattr__(self, name):
        if name == "data":
            return get_data_today()
        if name == "lines":
            return get_data_today().splitlines()
        if name == "ex":
            return get_ex_today()
        if name == "get":
            return get_data
        if name == "get_ex":
            return get_ex

        raise AttributeError(name)

sys.modules[__name__] = Aoc()