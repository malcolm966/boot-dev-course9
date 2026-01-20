import math


def prime_factors(n):
    prime_list = list()
    while n % 2 == 0:
        n /= 2
        prime_list.append(2)
    for num in range(3, int(n + 1), 2):
        i = math.sqrt(num)
        while n % i == 0:
            prime_list.append(i)
            n /= i
    if n > 2:
        prime_list.append(n)
    return list(sorted(prime_list))
    
