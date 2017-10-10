Each exercise in this section has two parts. Do the first part and once
everyone is done we'll talk through them and you can do the second part.


## Exercise A:
### Part One:
Take a string and filter it to include only every other character.

**Input Format**

A single string

**Expected Output**

A string consisting of the first character of the input, followed by the third
but not the second, the fifth but not the fourth, etc.

**Example**

```
> every_other_character('test')
'ts'
```

### Part Two:
Take a string and capitalize every other character.

**Input Format**

A single string in all lower case

**Expected Output**

A string consisting of the first character of the input followed by the second
character capitalized then the third uncapitalised, etc.

**Example**

```
> every_other_character_capitalized('test')
'tEsT'
```

## Exercise B:

### Part One:

Take a string and return it backwards.

**Input Format**

A single string.

**Expected Output**

A string consisting of the characters of the input in the reverse order.

**Example**

```
> reverse_string('test')
'tset'
```

### Part Two:

Take a string and swap each pair of characters.

**Input Format**

A single string.

**Expected Output**

A string consisting of the second character of the input followed by the first
followed by the fourth followed by the third etc. If the string has an odd
number of characters then the last character should be left unchanged.

**Example**

```
> swap_characters('test')
'etst'
> sway_characters('dog')
'odg'
```
## Exercise C:

### Part One:

Take a string and return all words it contains in reverse order. Where a word
is defined as a group of characters separated by spaces.

**Input Format**

A single string

**Expected Output**

A string consisting of the last word in the input followed by the second last etc.

**Example**

```
> reverse_words('the quick brown fox')
'fox brown quick then'
```

### Part Two:

Take a string and count how many times each character it contains appears.

**Input Format**

A single string

**Expeceted Output**

A dictionary where the keys are each unique character which appeared in the
input and the values are the number of times the character appeared.

**Example**

```
> count_characters('test')
{'t': 2, 'e': 1, 's': 1}
```
