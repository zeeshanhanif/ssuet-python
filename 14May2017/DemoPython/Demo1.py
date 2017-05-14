from functools import partial
def exp(base, power):
    return base ** power

two_to_the = partial(exp, 2) # is now a function of one variable
print(two_to_the(3))