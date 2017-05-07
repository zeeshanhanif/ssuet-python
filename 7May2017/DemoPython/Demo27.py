from functools import partial

def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2)
tw = partial(exp, power=2)
print(two_to_the(3))
print(tw(3))