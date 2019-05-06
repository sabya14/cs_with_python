from functools import partial


def currency_scaler(number, factor):
    return number * factor


def usd_to_rupees(number):
    return currency_scaler(number, 70)


def pound_to_rupees(number):
    return currency_scaler(number, 90)


amount_list = [100, 200, 300]
