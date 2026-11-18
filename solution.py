import itertools

def solve(value):
    return [{"character": c, "count": sum(1 for _ in group)} for c, group in itertools.groupby(value)]
