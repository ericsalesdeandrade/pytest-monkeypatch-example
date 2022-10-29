import time


def calculate_sum(a: int | float, b: int | float):
    delay()
    return f"Sum of the 2 Numbers is `{a + b}`"


def delay():
    print("5 Sec Delay....")
    time.sleep(5)
