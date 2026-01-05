import math


def get_influencer_score(num_followers, average_engagement_percentage):
    return math.log(num_followers,2) * average_engagement_percentage
