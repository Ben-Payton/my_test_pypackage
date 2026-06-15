import my_test_pypackage as my_test_pypackage


def test_add_success():
    assert my_test_pypackage.my_add(1, 2) == 3

def test_add_two():
    assert my_test_pypackage.my_add(4, 7) == 11
    assert my_test_pypackage.my_add(-3, 7) == 4
