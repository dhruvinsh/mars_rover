from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Union

from .directions import direction
from .exceptions import InvalidDirection, InvalidCoordinate


@dataclass
class Position:
    """Holder for coordinates of rover with rover direction where it facing to.
    object is aware of 4 directions only. else it will raise InvalidDirection
    exceptions.

    two object facing in same direction, addition is possible else raise
    InvalidDirection issue."""

    x: int
    y: int
    _direction: str = field(repr=False, default='N')

    def __post_init__(self):
        if not isinstance(self.x, int) or not isinstance(self.y, int):
            raise InvalidCoordinate("Invalid coordinates passed")
        self.direction = self._direction

    def __str__(self):
        return f"Position(x={self.x}, y={self.y}, direction={self.direction_to_string})"

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y}, direction={self.direction_to_string})"

    def __add__(self, other: Position) -> Position:
        """implement addition method for two position objects in same
        direction"""
        if self.direction != other.direction:
            raise InvalidDirection(
                'Addition is not possible for two different direction')
        self.x += other.x
        self.y += other.y
        return self

    @property
    def direction(self) -> int:
        return self._direction

    @direction.setter
    def direction(self, value: Union[str, int]) -> None:

        if isinstance(value, str):
            if value not in direction:
                raise InvalidDirection(
                    "Subtraction is not possible for two different direction")
            self._direction = direction[value] * 90
        elif isinstance(value, int):
            self._direction = value

        logging.debug(f"Direction value set to: {self._direction}")

    @property
    def direction_to_string(self) -> str:
        """get direction degrees converted to N, E, S or W string"""
        facing = int((self.direction % 360) / 90)
        # direction reverse lookup
        return {v: k for k, v in direction.items()}.get(facing)
