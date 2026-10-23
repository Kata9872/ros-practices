
import math


LIMITS = {
    'linear_speed': (0.0, 1.0),
    'turn_rate': (-1.0, 1.0),
    'publish_hz': (1.0, 30.0),
}


def is_valid(name, value):
    if name not in LIMITS:
        return False

    if type(value) not in (int, float):
        return False

    low, high = LIMITS[name]
    return math.isfinite(value) and low <= value <= high
