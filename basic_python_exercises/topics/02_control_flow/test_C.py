import random
from itertools import combinations
from .C import possible_ingredients, determine_pizza_choices


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
        no_good_combos = [i for i in flattened_dislikes if isinstance(i, list)]
        final_ingredients = set(available_ingredients).difference(set(no_good))

        count = 0
        for i in range(1, len(final_ingredients)+1):
            for p in combinations(final_ingredients, i):
                pizza_good = True
                for c in no_good_combos:
                    if c in p:
                        pizza_good = False
                        break
                if pizza_good:
                    count += 1

        func_out = determine_pizza_choices(available_ingredients, dislikes)
        assert func_out == count
