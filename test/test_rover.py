import pytest
from robot import Rover, Position
from robot.exceptions import InvalidInstruction


@pytest.fixture
def _rover():
    origin = Position(2, 3, 'E')
    return Rover(origin)


def test_move_forward(_rover):
    _rover.move_forward()
    assert _rover.position.x == 3
    assert _rover.position.y == 3
    assert _rover.position.direction == 90


def test_left_turn(_rover):
    _rover.left_turn()
    assert _rover.position.x == 2
    assert _rover.position.y == 3
    assert _rover.position.direction == 0


def test_right_turn(_rover):
    _rover.right_turn()
    assert _rover.position.x == 2
    assert _rover.position.y == 3
    assert _rover.position.direction == 180


def test_process(_rover):
    instruction = 'LMLMLMLMMRRR'
    _rover.process(instruction)
    assert _rover.position.x == 3
    assert _rover.position.y == 3
    assert _rover.position.direction == 0


def test_invalid_command(_rover):
    instruction = 'LMLMA'
    with pytest.raises(InvalidInstruction):
        _rover.process(instruction)


def test_position_to_string(_rover, capsys):
    _rover.position_to_string()
    captured = capsys.readouterr()
    assert captured.out == "Rover is at: 2 3 E\n"
