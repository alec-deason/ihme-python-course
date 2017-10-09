import random
import math
from B import possible_ingredients, determine_pizza_choices


def test_determine_pizza_choices():
    for _ in range(100):
        num_people = random.randint(2, 8)
        available_ingredients = random.sample(possible_ingredients, random.randint(0, len(possible_ingredients)))
        dislikes = []

        for __ in range(num_people):
            dislikes.append(random.sample(available_ingredients, random.randint(0, len(possible_ingredients))))

        no_good = set(*dislikes)
        remaining_ingredients = set(available_ingredients).difference(no_good)
        func_out = determine_pizza_choices(available_ingredients, dislikes)
        assert func_out == math.factorial(len(remaining_ingredients))
