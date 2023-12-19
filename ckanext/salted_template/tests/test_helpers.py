"""Tests for helpers.py."""

import ckanext.salted_template.helpers as helpers


def test_salted_template_hello():
    assert helpers.salted_template_hello() == "Hello, salted_template!"
