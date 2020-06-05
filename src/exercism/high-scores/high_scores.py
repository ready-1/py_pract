def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    scores.reverse()
    if len(scores) < 4:
        return scores
    return scores[:3]
