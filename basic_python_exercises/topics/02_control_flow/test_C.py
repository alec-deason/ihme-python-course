import random
from .C import possible_ingredients, determine_pizza_choices

# TODO: Write this test
def test_determine_pizza_choices():
    for _ in range(100):
        num_people = random.randint(2, 8)
        available_ingredients = random.sample(possible_ingredients, random.randint(0, len(possible_ingredients)))
        dislikes = []

        for __ in range(num_people):
            dislikes.append(random.sample(available_ingredients, random.randint(0, len(possible_ingredients))))

        no_good = set(*dislikes)
        func_out = determine_pizza_choices(available_ingredients, dislikes)
        assert len(func_out) == len(set(func_out))
        assert set(func_out) == set(available_ingredients).difference(set(no_good))
