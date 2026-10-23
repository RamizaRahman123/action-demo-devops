"""Tests for main.py."""

from main import add, greet


def test_greet():
    """greet returns the expected message."""
    assert greet("DevOps") == "Hello, DevOps!"


def test_add():
    """add returns the sum of two numbers."""
    assert add(2, 3) == 5
