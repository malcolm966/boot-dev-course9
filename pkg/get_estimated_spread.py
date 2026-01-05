# estimated_spread = average_audience_followers * ( num_followers ^ 1.2 )
from sumed import summed
def get_estimated_spread(audiences_followers):
    if audiences_followers:
        num_followers = len(audiences_followers)
        average_audience_followers  = summed(audiences_followers) / num_followers
        estimated_spread = average_audience_followers * ( num_followers ** 1.2 )
        return estimated_spread
    return 0
