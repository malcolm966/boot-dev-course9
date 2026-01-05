# remaining_total = quantity * ( retention_rate ^ time )
def decayed_followers(initial_followers, fraction_lost_daily, days):
    retention_rate =  1 - fraction_lost_daily
    remaining_total = initial_followers * ( retention_rate ** days )
    return remaining_total


print(decayed_followers(100, 0.5,2))