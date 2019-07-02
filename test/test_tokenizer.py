import pytest
from robot import tokenize
from robot.exceptions import InvalidPlateauSize, InvalidInput

input_data = """
6 6

2 4 N
LMLMLM
"""

invalid_plateau_data = """
6

2 4 N
LMLMLM
"""

invalid_instruction_data = """
6 6

2 4 5 N
LMLMLM
"""

invalid_data = """
6 6

2 4 N
"""

def test_tokenize_valid_data():
    for x, y, direction, instruction in tokenize(input_data):
        assert x == 2
        assert y == 4
        assert direction == 'N'
        assert instruction == 'LMLMLM'


def test_tokenize_invalid_data():
    with pytest.raises(InvalidPlateauSize):
        next(tokenize(invalid_plateau_data))

    with pytest.raises(InvalidInput):
        next(tokenize(invalid_instruction_data))

    with pytest.raises(InvalidInput):
        next(tokenize(invalid_data))
