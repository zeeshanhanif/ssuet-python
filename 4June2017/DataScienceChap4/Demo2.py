data = [
    [26,30],
    [28,50],
    [30,70]
]

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    dotVal = [v_i * w_i
        for v_i, w_i in zip(v, w)]
    print("dotval ",dotVal)
    sum1 = sum(dotVal)
    print("dot product sum ", sum1)
    return sum1

#re1 = dot(data[0],data[1])
#print(re1);

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

import math
def magnitude(v):
    sum_of_sq = sum_of_squares(v)
    print("sum of squiare ",sum_of_sq)
    return math.sqrt(sum_of_squares(v))

mag = magnitude(data[0])
print(mag)

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
        for v_i, w_i in zip(v, w)]

def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    subtc = vector_subtract(v, w)
    print("verctor subtract ",subtc)
    return sum_of_squares(subtc);

def distance(v, w):
    return math.sqrt(squared_distance(v, w))


re3 = distance(data[0],data[1])
print("m1 ", re3)

re4 = distance(data[0],[27,40])
print("m2 ", re4)

re5 = distance(data[1],[27,40])
print("m3 ", re5)


from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(data[0],[27,40]))

print(cosine_similarity(data[1],[27,40]))