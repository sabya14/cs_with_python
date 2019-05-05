from functools import partial


def interest(p, r, t):
    print(p, r, t)
    return p * r * t / 100


interest_rate_10_year_1 = partial(interest, r=10, t=1)
interest_rate_10_year_3 = partial(interest, r=10, t=2)
interest_rate_10_year_5 = partial(interest, r=10, t=3)

principal_list = [100, 200, 300]
print(list(map(lambda x: interest_rate_10_year_1(x), principal_list)))

