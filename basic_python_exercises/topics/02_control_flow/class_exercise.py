#TODO: finish doc string
"""Pizza with friends.

You are hanging out with two of your friends, and you decide to order pizza.
Each of you is pretty open to most pizza toppings, but you all have a few that you
are either allergic to or that you intensely dislike.  You've gone out to the
pizza restaurant's website to get a list of their ingredients and now you want
to figure out all the different kinds of pizza you can order given everyone's preferences.

For example:

Say we have the ingredient list from the restaurant as follows:

ingredients = ['pepperoni', 'sausage', 'mushrooms', 'black olives', 'green peppers', 'onions', 'pineapple']

"""

# TODO: Rephrase this so the output is a list of lists of ingredients, each representing a different pizza.

meats = ['pepperoni', 'bacon', 'beef', 'sausage', 'italian sausage', 'meatballs', 'salami', 'ham', 'anchovies', ]
veggies = ['mushrooms', 'onions', 'black olives', 'pineapple', 'jalepenos', 'tomatoes', 'green peppers',
           'red onions', 'banana peppers', 'garlic', ]
cheeses = ['mozzarella', 'parmesan', 'romano', 'asiago']
sauces = ['tomato', 'bbq', 'ranch', ]
available_ingredients = meats + veggies + cheeses + sauces


def determine_pizza_choices(your_dislikes, friend_1_dislikes, friend_2_dislikes):
    return
