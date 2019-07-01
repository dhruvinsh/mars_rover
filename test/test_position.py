import pytest
from robot import Position
from robot.exceptions import InvalidCoordinate


def test_valid_position():
    origin = Position(1, 2, 'E')
    assert origin.x == 1
    assert origin.y == 2
    assert origin.direction == 90


def test_invalid_position():
    with pytest.raises(InvalidCoordinate):
        Position(1.1, 2, 'W')

def test_direction_to_string():
    origin = Position(1, 2)
    assert origin.direction == 0
    assert origin.direction_to_string == "N"
