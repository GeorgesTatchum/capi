def apply_rule(rule, votes):
    if rule == "Majorité absolue":
        return absolute_majority_rule(votes)
    elif rule == "Majorité relative":
        return relative_majority_rule(votes)
    else:
        raise ValueError("Règle inconnue")


def absolute_majority_rule(votes):
    majority = len(votes) // 2
    counts = {vote: votes.count(vote) for vote in set(votes)}
    estimate = next((vote for vote, count in counts.items() if count > majority), None)
    return {"validated": estimate is not None, "estimate": estimate}


def relative_majority_rule(votes):
    counts = {vote: votes.count(vote) for vote in set(votes)}
    estimate = max(counts, key=counts.get)
    return {"validated": True, "estimate": estimate}
