from A import course_tester

def test_course_tester():
    courses = [['a', 'b'], ['b', 'c'], ['c', 'd']]
    assert course_tester(courses)

    courses = [['a','b','c']]*1000
    assert course_tester(courses)

    courses = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    assert not course_tester(courses)

    courses = [[],['a', 'b'],['b']]
    assert not course_tester(courses)

    assert not course_tester([[i] for i in range(1000)])
