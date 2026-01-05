import math

def log_scale(data, base):
    return list(map(lambda x : math.log(x, base), data))