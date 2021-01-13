import pytest
from py_src_dir_layout.hello import say


def test_say():
    assert "Hello" == say("Hello")
