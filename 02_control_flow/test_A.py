import random
import math
from A import possible_ingredients, determine_pizza_choices


def test_determine_pizza_choices():
    for _ in range(100):
        available_ingredients = random.sample(possible_ingredients, random.randint(0, len(possible_ingredients)))
        your_dislikes = random.sample(available_ingredients, random.randint(0, len(possible_ingredients)))
        friend_1_dislikes = random.sample(available_ingredients, random.randint(0, len(possible_ingredients)))
        friend_2_dislikes = random.sample(available_ingredients, random.randint(0, len(possible_ingredients)))

        no_good = set(your_dislikes + friend_1_dislikes + friend_2_dislikes)
        remaining_ingredients = set(available_ingredients).difference(no_good)
        func_out = determine_pizza_choices(your_dislikes, friend_1_dislikes, friend_2_dislikes)
        assert func_out == math.factorial(len(remaining_ingredients))
