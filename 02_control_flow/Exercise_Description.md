## Exercise A:

Given a variable input list of ingredients in addition to the lists of dislikes you
and your friends share, determine the number of different pizzas you can order.

**Input Format**

Four lists.  The first list contains the ingredients available at the pizza place
you're ordering from.  The next three lists contain the dislikes of you and your friends.

**Expected Output**

The number of possible pizza combinations you can order.

**Example**

Say we have the following inputs
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

```['pepperoni', 'black_olives', 'mozzarella', 'tomato_sauce']```

and there are `4! = 4*3*2*1 = 24` ways we can uniquely combine 4 ingredients.


## Exercise B:

You're trying to generalize a bit and you decide you want a tool that can tell you
the number of pizzas you can order regardless of how many friends you're trying to 
order for.


**Input Format**

Two lists.  The first is a list of the available ingredients and the second
is a list of lists of the dislikes of all the friends you're ordering for.

**Expected Output** 

The number of possible pizza combinations you can order.

**Example**

Say we have the following inputs
```
ingredient_list = ['pepperoni', 'bacon', 'beef', 'sausage',
                   'mushrooms', 'onions', 'black olives', 'pineapple', 
                   'mozzarella', 'tomato_sauce']
list_of_dislikes = [['beef', 'mushrooms', 'pineapple'], ['bacon', 'pineapple'], ['beef', 'sausage', 'onions']]
```

Then
 
```
determine_pizza_choices(ingredient_list, list_of_dislikes) = 24  
```
Since after removing all the disliked ingredients we have the remaining list

```['pepperoni', 'black_olives', 'mozzarella', 'tomato_sauce']```

and there are `4! = 4*3*2*1 = 24` ways we can uniquely combine 4 ingredients.

## Exercise C:

Turns out you have some complicated friends who are fine with some ingredients,
but are unhappy with particular combinations of ingredients.  Being a good friend,
you decide to try to accommodate them.  

**Input Format** 

Two lists.  The first is a list of the available ingredients and the second
is a list of lists of the dislikes of all the friends you're ordering for. Each of 
these sublists will contain strings for ingredients that the person absolutely 
won't eat and lists containing combinations of ingredients they won't eat.  For instance, 
say you have a friend who doesn't like black olives, onions, or pizzas with beef and mushrooms
on them in combination.  Their list of dislikes would look like

`['black_olives', 'onions', ['beef', 'mushrooms']]`

**Expected Output**

The number of possible pizza combinations you can order.

**Example**
Say we have the following inputs
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

```['pepperoni', 'sausage', 'onions', 'black_olives', 'mozzarella', 'tomato_sauce']```

for which there are `6! = 6*5*4*3*2*1 = 720` combinations.  However there are `4! + 1 = 25`
pizzas with both 'pepperoni' and 'black olives' on them, so we remove those to obtain
the `695` combinations.

and there are `4! = 4*3*2*1 = 24` ways we can uniquely combine 4 ingredients.
