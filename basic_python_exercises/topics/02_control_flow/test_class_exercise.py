import random
import math

from class_exercise import available_ingredients, determine_pizza_choices


def test_determine_pizza_choices():
    for _ in range(100):
        your_dislikes = random.sample(available_ingredients, random.randint(0, len(available_ingredients)))
        friend_1_dislikes = random.sample(available_ingredients, random.randint(0, len(available_ingredients)))
        friend_2_dislikes = random.sample(available_ingredients, random.randint(0, len(available_ingredients)))

        no_good = set(your_dislikes + friend_1_dislikes + friend_2_dislikes)
        remaining_ingredients = set(available_ingredients).difference(no_good)
        func_out = determine_pizza_choices(your_dislikes, friend_1_dislikes, friend_2_dislikes)
        assert func_out == math.factorial(len(remaining_ingredients))
