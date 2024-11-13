from app.rules import apply_rule


def test_absolute_majority_rule():
    votes = [3, 3, 5, 3]
    result = apply_rule("Majorité absolue", votes)
    assert result["validated"] == True
    assert result["estimate"] == 3

    votes = [3, 3, 5, 5]
    result = apply_rule("Majorité absolue", votes)
    assert result["validated"] == False


def test_relative_majority_rule():
    votes = [3, 3, 5, 3]
    result = apply_rule("Majorité relative", votes)
    assert result["validated"] == True
    assert result["estimate"] == 3

    votes = [3, 3, 5, 5]
    result = apply_rule("Majorité relative", votes)
    assert result["validated"] == True
    assert result["estimate"] == 3 or result["estimate"] == 5
