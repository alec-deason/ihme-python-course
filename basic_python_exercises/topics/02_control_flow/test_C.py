import random
import math
from .C import possible_ingredients, determine_pizza_choices

# TODO: Write this test
def test_determine_pizza_choices():
    for _ in range(100):
        num_people = random.randint(2, 5)
        available_ingredients = random.sample(possible_ingredients,
                                              random.randint(len(possible_ingredients)/2, len(possible_ingredients)))
        dislikes = []

        for __ in range(num_people):
            person_dislikes = random.sample(available_ingredients, random.randint(0, len(possible_ingredients)))
            if random.random() > 0.5:
                while True:
                    # For about half the people, add a 2-3 ingredient combos that they dislike.
                    person_dislikes.append(random.sample(available_ingredients, random.randint(2, 3)))
                    if random.random() < 0.8:
                        # 10 percent of the time they have more than one combo they dislike
                        break
            dislikes.append(person_dislikes)

        flattened_dislikes = [i for person_dislikes in dislikes for i in person_dislikes]
        no_good = set([i for i in flattened_dislikes if isinstance(i, str)])
        no_good_combos_start = [i for i in flattened_dislikes if isinstance(i, list)]

        # Remove duplicates and unavailable ingredient combinations
        no_good_combos = []
        for combo in no_good_combos_start:
            combo_contains_unavailable_ingredients = [ingredient for ingredient in combo if ingredient in no_good]
            if combo not in no_good_combos and not combo_contains_unavailable_ingredients:
                no_good_combos.append(combo)

        final_ingredients = set(available_ingredients).difference(set(no_good))
        num_combos = math.factorial(len(final_ingredients))
        num_bad_combos = 0
        for combo in no_good_combos:
            # FIXME: This overcounts the bad combos
            num_bad_combos += math.factorial(len(final_ingredients) - len(combo)) + 1

        func_out = determine_pizza_choices(available_ingredients, dislikes)
        assert func_out == num_combos - num_bad_combos
