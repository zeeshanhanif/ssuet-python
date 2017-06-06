data = [
    [26,30],
    [28,50],
    [30,70]
]

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
        for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
        for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0] # start with the first vector
    for vector in vectors[1:]: # then loop over the others
        result = vector_add(result, vector) # and add them to the result
    return result

re = vector_sum(data);
print(re);

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

r3 = vector_mean(data);
print(r3)

