import pytest
from rocket_science.hello import say


def test_say():
    assert "Hello" == say("Hello")
