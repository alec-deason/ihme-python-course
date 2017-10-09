def course_tester(courses):
    """
    You're designing the menu at a fancy restaurant and it's important to you
    that the courses be linked together by common ingredients. So, the first
    course and the second course must share an ingredient, the second and the
    third course must share an ingredient, etc. Write a function that tests
    a menu to make sure this condition is met.

    `courses` will be a list containing the description of each course in the
    form of a list of ingredients it uses. For example:
        [
          ['jello', 'marshmallow', 'canned fruit'],
          ['elbow macaroni', 'american cheese', 'margarine'],
          ['flour', 'sugar', 'margarine', 'egg', 'whipped topping'],
        ]

    This menu does not meet the constraint since the first and second course
    share no ingredients.

    Your implementation should return `True` in the case where the constraint is
    met and `False` otherwise.

    Examples
    --------
    course_tester([
                   ['apple', 'cheese'],
                   ['lettuce', 'cheese', 'walnut', 'chicken'],
                   ['walnut', 'cream', 'sugar']]) -> True
    course_tester([
                   ['spinach', 'feta'],
                   ['tomato', 'stock', 'bean', 'lamb'],
                   ['cream', 'chocolate', 'sugar']) -> False
    """

    return False
