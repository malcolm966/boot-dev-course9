# from enum import Enum

# INFLUENCER = Enum('INFLUENCER',['fitness','cosmetic'])

def get_follower_prediction(follower_count:int, influencer_type:str, num_months:int):
    total = 0
    match influencer_type:
        case 'fitness':
            total = follower_count * (4 ** num_months)
        case 'cosmetic':
            total = follower_count * (3 ** num_months)
        case _:
            total = follower_count * (2 ** num_months)
    return total