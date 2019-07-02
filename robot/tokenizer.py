from .exceptions import InvalidInput, InvalidPlateauSize
from .position import Position


def tokenize(data: str):
    """this generator allow to break data into object understandable data.
    input data expected as below,
    5 5

    1 2 N
    LMLMLMLMM

    3 3 E
    MMRMMRMRRM

    Here the first line is plateau size, followed by group of 2 data lines,
    Which are rover's instructions set. First line gives rover origin position
    and second is instruction command set.

    yield are: x, y, direction and instruction
    """
    data = data.split('\n')
    data = [i.strip() for i in data if i]

    plateau_size = data[0].split()
    if len(plateau_size) != 2:
        raise InvalidPlateauSize("first line do not have plateau size")

    plateau_size = Position(x=int(plateau_size[0]), y=int(plateau_size[1]))
    data.pop(0)

    # lets check for valid input data
    if len(data) % 2 != 0:
        raise InvalidInput("invalid input data detected")

    for i in range(0, len(data), 2):
        try:
            x, y, direction = data[i].split()
            instruction = data[i + 1]
            yield int(x), int(y), direction, instruction
        except ValueError:
            raise InvalidInput("Invalid input data detected")
