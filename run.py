import logging

from data import data
from robot import Position, Rover, tokenize

logging.basicConfig(level=logging.DEBUG)

for x, y, direction, instruction in tokenize(data):
    origin = Position(x, y, direction)
    rover = Rover(origin)
    rover.process(instruction)
    rover.position_to_string()
