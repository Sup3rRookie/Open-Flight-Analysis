import main, pytest

""" Unit Test """
def test_distance_negative():
    try:
        main.distance_between_each_airports('Random Airport')
    except ValueError:
        assert True

def test_distance_positive():
    pass

def test_counts_of_airports():
    result = main.count_all_airports_in_malaysia()
    assert result == 40
