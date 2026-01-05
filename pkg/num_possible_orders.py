def num_possible_orders(num_posts):
    product = 1
    for i in range(2, num_posts + 1):
        product *= i
    return product

