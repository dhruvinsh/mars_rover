class InvalidDirection(ValueError):
    """Throw an exception when invalid direction passed"""


class InvalidInput(ValueError):
    """Throw an exception when invalid input data is provided"""


class InvalidCoordinate(ValueError):
    """Throw an exception when invalid coordinates data is provided"""


class InvalidInstruction(InvalidInput):
    """Throw an exception when invalid instruction data detected"""


class InvalidPlateauSize(InvalidInput):
    """Throw an exception when invalid input data detected"""
