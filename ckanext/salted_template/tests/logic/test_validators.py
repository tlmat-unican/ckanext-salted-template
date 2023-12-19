"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.salted_template.logic import validators


def test_salted_template_reauired_with_valid_value():
    assert validators.salted_template_required("value") == "value"


def test_salted_template_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.salted_template_required(None)
