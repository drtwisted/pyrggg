from random import sample


def get_random_numbers(top_margin, count):
    res = list()

    if count > top_margin:
        itters = count // top_margin
        for _ in range(itters):
            res.extend(sample(range(top_margin), top_margin))
        res.extend(sample(range(top_margin), count - (top_margin * itters)))
    else:
        res = sample(range(top_margin), count)

    return res
