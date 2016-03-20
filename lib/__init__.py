from random import randrange, sample, seed
from time import clock


def get_random_numbers(top_margin, count):
    seed(clock())
    res = list()

    if count > top_margin:
        itters = count // top_margin
        for _ in range(itters):
            res.extend(sample(range(top_margin), top_margin))
        res.extend(sample(range(top_margin), count - (top_margin * itters)))
    else:
        res = sample(range(top_margin), count)

    return res


def get_rand(top_margin, low_margin=0):
    seed(clock())
    top_margin = top_margin if top_margin >= low_margin else low_margin
    return randrange(low_margin, top_margin)
