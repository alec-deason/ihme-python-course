"""
Exercise B
==========
You're trying to generalize a bit and you decide you
want a tool that can tell you the number of pizzas you can
order regardless of how many friends you're trying to order for.

Input Format
------------
Two lists. The first is a list of the available ingredients and
the second is a list of lists of the dislikes of all the friends you're ordering for.

Expected Output
---------------
The number of possible pizza combinations you can order.

Example
-------
Say we have the following inputs:

```
ingredient_list = ['pepperoni', 'bacon', 'beef', 'sausage',
                   'mushrooms', 'onions', 'black olives', 'pineapple',
                   'mozzarella', 'tomato_sauce']
list_of_dislikes = [['beef', 'mushrooms', 'pineapple'], ['bacon', 'pineapple'], ['beef', 'sausage', 'onions']]
```

Then

```
determine_pizza_choices(ingredient_list, your_dislikes, friend_1_dislikes, friend_2_dislikes) = 24
```

Since after removing all the disliked ingredients we have the remaining list

['pepperoni', 'black_olives', 'mozzarella', 'tomato_sauce']

and there are 4! = 4*3*2*1 = 24 ways we can uniquely combine 4 ingredients.
"""

meats = ['pepperoni', 'bacon', 'beef', 'sausage', 'italian sausage', 'meatballs', 'salami', 'ham', 'anchovies', ]
veggies = ['mushrooms', 'onions', 'black olives', 'pineapple', 'jalepenos', 'tomatoes', 'green peppers',
           'red onions', 'banana peppers', 'garlic', ]
cheeses = ['mozzarella', 'parmesan', 'romano', 'asiago']
sauces = ['tomato', 'bbq', 'ranch', ]
possible_ingredients = meats + veggies + cheeses + sauces

# The ingredient list and the lists of dislikes will all come from the list of possible ingredients.

def determine_pizza_choices(ingredient_list, list_of_dislikes):
    return
