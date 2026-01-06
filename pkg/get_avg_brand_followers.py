def get_avg_brand_followers(all_handles, brand_name):
    total_handles = 0
    loyal_handles = 0

    for user_handles in all_handles:
        total_handles += 1
        for handle in user_handles:
            if brand_name in handle:
                loyal_handles += 1

    if total_handles == 0:
        return 0

    return loyal_handles / total_handles