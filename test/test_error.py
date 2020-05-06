#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the openxr.error module."""

from openxr import Error

def test_result():
    assert(Error(42).result == 42)

if __name__ == '__main__':
    import pytest, sys

    sys.exit(pytest.main(__file__))
