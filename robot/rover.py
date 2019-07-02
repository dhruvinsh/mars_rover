import logging
from math import sin, cos, radians
from dataclasses import dataclass

from .position import Position
from .exceptions import InvalidInstruction

VALID_COMMAND = ["L", "R", "M"]


@dataclass
class Rover:
    """This class mimic mars rover. It can process the instruction and can
    perform movements like turn left or right or move forward. Instruction
    looks like combinations of LRM, where "L" and "R" is for left and right
    turn respectively.

    Class initialized with its Positional object.

    Usage:
    >>> from robot import Position
    >>> from robot import Rover
    >>> origin = Position(1, 1, 'E')
    >>> rover = Rover(origin)
    >>> rover.left_turn()
    >>> rover.move_forward()
    >>> rover.position_to_string()
    Rover is at: 1 2 N
    """

    position: Position

    def move_forward(self, step: int = 1):
        """rover action: move forward
        param: step: for a defined direction how many step to move default is
                     set to 1 step only.
        """
        x = step * sin(radians(self.position.direction))
        y = step * cos(radians(self.position.direction))
        new_position = Position(int(x), int(y), self.position.direction)
        self.position = self.position + new_position
        logging.debug(f"new position after moving forward: {self.position}")

    def left_turn(self) -> None:
        """rover action: take left turn
        this will change the rover direction by -90(negative) degrees without
        moving from its place"""
        self.position.direction -= 90

    def right_turn(self) -> None:
        """rover action: take right turn
        this will change the rover direction by 90(negative) degrees without
        moving from its place"""
        self.position.direction += 90

    def process(self, instruction: str) -> None:
        """rover action: perform multiple instruction set automatically
        param: instruction: expect to receive information in form of LRM
                            combinations. eg. "LMMRMMMR"
        """
        logging.info(f"instruction to process: {instruction}")
        instruction = list(instruction.upper())
        for cmd in instruction:
            if cmd not in VALID_COMMAND:
                raise InvalidInstruction(
                    f"Command: {instruction} is not valid")

            if cmd == 'L':
                self.left_turn()
            elif cmd == 'R':
                self.right_turn()
            elif cmd == 'M':
                self.move_forward()

    def position_to_string(self) -> None:
        """allows to print rover location and direction in string format, like
        1 3 N. where x coordinate: 1, y coordinate: 3, facing: N"""
        x = self.position.x
        y = self.position.y
        direction = self.position.direction_to_string
        print(f"Rover is at: {x} {y} {direction}")
