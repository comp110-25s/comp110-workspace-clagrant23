import pytest

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


"""For each function, 3x unit test functions are defined"""

__author__ = "730567639"


def test_invert_empty():
    assert invert({}) == {}


def test_invert_michael_jordan():
    assert invert({"Michael": "Jordan"}) == {"Jordan": "Michael"}


def test_invert_multiple_pairs():
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_keyworderror():
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_empty():
    assert count([]) == {}


def test_count_one_each():
    assert count(["red", "orange", "green", "blue"]) == {
        "red": 1,
        "orange": 1,
        "green": 1,
        "blue": 1,
    }


def test_count_multiple_of_each():
    assert count(["red", "green", "red", "blue", "green", "red"]) == {
        "red": 3,
        "green": 2,
        "blue": 1,
    }


def test_favorite_color_empty():
    assert favorite_color({}) == ""


def test_favorite_color_tie():
    assert (
        favorite_color({"clay": "blue", "alexa": "purple", "mason": "orange"}) == "blue"
    )


def test_favorite_color_winner():
    assert (
        favorite_color({"clay": "blue", "alexa": "purple", "mason": "purple"})
        == "purple"
    )


def test_bin_len_empty():
    assert bin_len([]) == {}


def test_bin_len_diff_lens():
    assert bin_len(["the", "bear"]) == {3: {"the"}, 4: {"bear"}}


def test_bin_len_same_lens():
    assert bin_len(["the", "big", "bear"]) == {3: {"the", "big"}, 4: {"bear"}}
