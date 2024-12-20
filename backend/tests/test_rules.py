import pytest
from app.rules import (
    absolute_majority_rule,
    apply_rule,
    average_rule,
    median_rule,
    relative_majority_rule,
    strict_rule,
)


def test_strict_rule():
    assert strict_rule([1, 1, 1]) == {"validated": True, "estimate": 1}
    assert strict_rule([1, 2, 1]) == {"validated": False, "estimate": None}


def test_absolute_majority_rule():
    assert absolute_majority_rule([1, 2, 2, 2]) == {"validated": True, "estimate": 2}
    assert absolute_majority_rule([1, 2, 3, 4]) == {
        "validated": False,
        "estimate": None,
    }


def test_relative_majority_rule():
    assert relative_majority_rule([1, 2, 2, 3]) == {"validated": True, "estimate": 2}
    assert relative_majority_rule([1, 2, 2, 3, 3]) == {
        "validated": True,
        "estimate": 3,
    }  # Moyenne des votes gagnants


def test_median_rule():
    assert median_rule([1, 2, 3, 4, 5]) == {"validated": True, "estimate": 3}
    assert median_rule([1, 2, 3, 4]) == {"validated": True, "estimate": 2.5}


def test_average_rule():
    assert average_rule([1, 2, 3, 4, 5]) == {"validated": True, "estimate": 3}
    assert average_rule([1, 2, 3, 4]) == {"validated": True, "estimate": 3}


def test_apply_rule():
    votes = [1, 2, 2, 3]
    assert apply_rule(votes, "strict") == {"validated": False, "estimate": None}
    assert apply_rule(votes, "maj_absolue") == {"validated": False, "estimate": None}
    assert apply_rule(votes, "maj_relative") == {"validated": True, "estimate": 2}
    assert apply_rule(votes, "mediane") == {"validated": True, "estimate": 2}
    assert apply_rule(votes, "moyenne") == {"validated": True, "estimate": 2}

    with pytest.raises(ValueError):
        apply_rule(votes, "invalid_rule")
