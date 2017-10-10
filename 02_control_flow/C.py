"""
Exercise C
==========
Turns out you have some complicated friends who are fine with some ingredients,
but are unhappy with particular combinations of ingredients.
Being a good friend, you decide to try to accommodate them.

Input Format
------------
Two lists. The first is a list of the available ingredients and
the second is a list of lists of the dislikes of all the friends
you're ordering for. Each of these sublists will contain strings
for ingredients that the person absolutely won't eat and lists
containing combinations of ingredients they won't eat. For instance,
say you have a friend who doesn't like black olives, onions, or pizzas
with beef and mushrooms on them in combination. Their list of
dislikes would look like

```
['black_olives', 'onions', ['beef', 'mushrooms']]
```

Expected Output
---------------
The number of possible pizza combinations you can order.

Example
-------
Say we have the following inputs:

```
ingredient_list = ['pepperoni', 'bacon', 'beef', 'sausage',
                   'mushrooms', 'onions', 'black olives',
                   'pineapple', 'mozzarella', 'tomato_sauce']
list_of_dislikes = [['mushrooms', 'pineapple', 'beef'],
                    ['bacon', 'pineapple', ['pepperoni', 'black olives'], ['mushrooms', 'sausage']]]
```

Then

```
determine_pizza_choices(ingredient_list, list_of_dislikes) = 695
```

Since after removing all the individual disliked ingredients we have the remaining list

['pepperoni', 'sausage', 'onions', 'black_olives', 'mozzarella', 'tomato_sauce']

for which there are 6! = 6*5*4*3*2*1 = 720 combinations. However there are 4! + 1 = 25
pizzas with both 'pepperoni' and 'black olives' on them, so we remove those to obtain the 695 combinations.
"""

meats = ['pepperoni', 'bacon', 'beef', 'sausage', 'italian sausage', 'meatballs', 'salami', 'ham', 'anchovies', ]
veggies = ['mushrooms', 'onions', 'black olives', 'pineapple', 'jalepenos', 'tomatoes', 'green peppers',
           'red onions', 'banana peppers', 'garlic', ]
cheeses = ['mozzarella', 'parmesan', 'romano', 'asiago']
sauces = ['tomato', 'bbq', 'ranch', ]
possible_ingredients = meats + veggies + cheeses + sauces


def determine_pizza_choices(ingredient_list, list_of_dislikes):
    return
