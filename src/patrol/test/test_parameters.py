
from patrol.validation import is_valid


def test_parameters():
    assert is_valid('publish_hz', 10.0)
    assert is_valid('publish_hz', 5.0)

    assert not is_valid('publish_hz', 0.0)
    assert not is_valid('publish_hz', -1.0)
    assert not is_valid('publish_hz', float('nan'))

    assert is_valid('linear_speed', 0.5)
    assert not is_valid('linear_speed', 2.0)

    assert is_valid('turn_rate', -1.0)
    assert not is_valid('turn_rate', 2.0)
