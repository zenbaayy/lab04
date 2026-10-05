"""Lab 04 - Lab Tasks 1, 2, 4: password validator tests."""

import pytest

from password_validator import MAX_LENGTH, is_valid_password, validate_password


@pytest.fixture
def valid_password():
    """Lab Task 4: reusable fixture that gives a known-good password."""
    return "Strong#Pass1"


# ---- normal cases ----
def test_valid_password_accepted(valid_password):
    assert validate_password(valid_password) == []


def test_is_valid_password_true(valid_password):
    assert is_valid_password(valid_password) is True


# ---- boundary cases ----
def test_exactly_min_length_allowed():
    assert is_valid_password("Abcdef1!")  # 8 chars


def test_one_below_min_length_rejected():
    assert "too short" in validate_password("Abcde1!")  # 7 chars


def test_exactly_max_length_allowed():
    pwd = "Aa1!" + "x" * (MAX_LENGTH - 4)
    assert len(pwd) == MAX_LENGTH
    assert is_valid_password(pwd)


def test_one_above_max_length_rejected():
    pwd = "Aa1!" + "x" * (MAX_LENGTH - 3)
    assert "too long" in validate_password(pwd)


# ---- invalid inputs ----
def test_missing_uppercase(valid_password):
    assert "missing uppercase" in validate_password(valid_password.lower())


def test_missing_lowercase(valid_password):
    assert "missing lowercase" in validate_password(valid_password.upper())


def test_missing_digit():
    assert "missing digit" in validate_password("Strong#Pass")


def test_missing_special_character():
    assert "missing special character" in validate_password("StrongPass1")


def test_space_rejected():
    assert "contains space" in validate_password("Strong #Pass1")


def test_empty_string_rejected():
    assert not is_valid_password("")


def test_multiple_errors_reported():
    errors = validate_password("abc")
    assert {"too short", "missing uppercase", "missing digit"} <= set(errors)


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        validate_password(12345678)
