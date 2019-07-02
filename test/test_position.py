import pytest
from robot import Position
from robot.exceptions import InvalidCoordinate, InvalidDirection


def test_valid_position():
    origin = Position(1, 2, 'E')
    assert origin.x == 1
    assert origin.y == 2
    assert origin.direction == 90


def test_invalid_position():
    with pytest.raises(InvalidCoordinate):
        Position(1.1, 2, 'W')


def test_position_direction():
    origin = Position(1, 2)
    assert origin.direction == 0
    assert origin.direction_to_string == "N"


def test_direction_assignment():
    origin = Position(2, 3)
    assert origin.direction == 0

    origin.direction = 'S'
    assert origin.direction == 180
    assert origin.direction_to_string == 'S'

    origin.direction = -90
    assert origin.direction == -90
    assert origin.direction_to_string == 'W'


def test_invalid_str_direction():
    with pytest.raises(InvalidDirection):
        Position(1, 1, 'Q')


def test_invalid_int_direction():
    with pytest.raises(InvalidDirection):
        Position(1, 3, 110)


def test_postion_addition():
    pos_1 = Position(1, 1, 'S')
    pos_2 = Position(1, 1, 'S')
    addition = pos_1 + pos_2
    assert addition == Position(2, 2, 'S')


def test_invalid_postion_addition():
    pos_1 = Position(1, 1, 'S')
    pos_2 = Position(1, 1, 'E')
    with pytest.raises(InvalidDirection):
        pos_1 + pos_2


def test_str_position(capsys):
    print(Position(1, 1))
    captured = capsys.readouterr()
    assert captured.out == "Position(x=1, y=1, direction=N)\n"

    print(repr(Position(1, 2)))
    captured = capsys.readouterr()
    assert captured.out == "Position(x=1, y=2, direction=N)\n"
