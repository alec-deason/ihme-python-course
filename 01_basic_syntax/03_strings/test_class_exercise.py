from class_exercise import print_hello_world, print_hello_person, print_characters, print_characters_by_index

def test_print_hello_world(capfd):
    print_hello_world()
    out, err = capfd.readouterr()
    assert out == 'Hello, World!\n'

def test_print_hello_person(capfd):
    for name in ['Jane', 'John', '', 'a'*1000]:
        print_hello_person(name)
        out, err = capfd.readouterr()
        assert out == 'Hello, {}\n'.format(name)

def test_print_characters(capfd):
    for s in ['test', 'the quick brown fox']:
        print_characters(s)
        out, err = capfd.readouterr()
        assert out == ('\n'.join(list(s))+'\n')

def test_print_characters_by_index(capfd):
    for s in ['test', 'the quick brown fox']:
        print_characters_by_index(s)
        out, err = capfd.readouterr()
        assert out == ('\n'.join(list(s))+'\n')
