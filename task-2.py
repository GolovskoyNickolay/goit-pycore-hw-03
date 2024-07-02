import random
from typing import List


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    if min >= max:
        print("min must be less than max")
        return []
    elif min < 1:
        print("min must be more than 1")
        return []
    elif max > 1000:
        print("max must be less than 1000")
        return []
    elif (max - min) < quantity:
        print("quantity must be within min and max")
        return []
    else:
        random_list = random.sample(range(min, max), quantity)
        return sorted(random_list)


print(get_numbers_ticket(1, 49, 6))
