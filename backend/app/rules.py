from statistics import mean, median


def apply_rule(votes: list, rule: str = "strict"):
    if rule == "maj_absolue":
        return absolute_majority_rule(votes)
    elif rule == "maj_relative":
        return relative_majority_rule(votes)
    elif rule == "strict":
        return strict_rule(votes)
    elif rule == "mediane":
        return median_rule(votes)
    elif rule == "moyenne":
        return average_rule(votes)
    else:
        raise ValueError("règle inconnue")


def strict_rule(votes: list):
    if len(set(votes)) == 1:
        return {"validated": True, "estimate": votes[0]}
    return {"validated": False, "estimate": None}


def absolute_majority_rule(votes):
    total_votes = len(votes)
    majority_threshold = total_votes // 2 + 1
    vote_counts = {}

    for vote in votes:
        vote_counts[vote] = vote_counts.get(vote, 0) + 1
        if vote_counts[vote] >= majority_threshold:
            return {"validated": True, "estimate": vote}

    return {"validated": False, "estimate": None}


def relative_majority_rule(votes):
    vote_counts = {}
    for vote in votes:
        vote_counts[vote] = vote_counts.get(vote, 0) + 1

    max_count = max(vote_counts.values())
    winning_votes = [vote for vote, count in vote_counts.items() if count == max_count]

    if len(winning_votes) == 1:
        return {"validated": True, "estimate": winning_votes[0]}
    else:
        # En cas d'égalité, on prend la moyenne des votes gagnants
        return {"validated": True, "estimate": round(mean(winning_votes))}


def median_rule(votes):
    med = median(votes)
    return {"validated": True, "estimate": med}


def average_rule(votes):
    avg = round(mean(votes))
    return {"validated": True, "estimate": avg}
