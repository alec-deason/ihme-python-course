"""
Exercise A
==========

Given a variable input list of ingredients in addition to the lists
of dislikes you and your friends share, determine the number of different pizzas you can order.

Input Format
------------
Four lists. The first list contains the ingredients available at the pizza
place you're ordering from. The next three lists contain the dislikes of you and your friends.

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
your_dislikes = ['beef', 'mushrooms', 'pineapple']
friend_1_dislikes = ['bacon', 'pineapple']
friend_2_dislikes = ['beef', 'sausage', 'onions']
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
sauces = ['tomato_sauce', 'bbq_sauce', 'ranch_sauce', ]
possible_ingredients = meats + veggies + cheeses + sauces

# The ingredient list and the lists of dislikes will all come from the list of possible ingredients.

def determine_pizza_choices(ingredient_list, your_dislikes, friend_1_dislikes, friend_2_dislikes):
    return
