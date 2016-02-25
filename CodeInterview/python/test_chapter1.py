# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:27:21 2016

@author: espang
"""
import chapter1


def test_is_unique():
    assert chapter1.is_unique('asdf') == True
    assert chapter1.is_unique('asdaf') == False
    assert chapter1.is_unique('\nasdf\n') == False


def test_is_permutation():
    assert chapter1.is_permutation('asdf', 'sdaf') == True
    assert chapter1.is_permutation('asdf', 'asdfa') == False
    assert chapter1.is_permutation('asdf', 'asdd') == False


def test_urlify():
    assert chapter1.urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
    assert chapter1.urlify(' Mr John Smith      ', 14) == '%20Mr%20John%20Smith'


def test_is_permutation_of_palindrom():
    assert chapter1.is_permutation_of_palindrom('taco cat') == True
    assert chapter1.is_permutation_of_palindrom('taco catt') == False


def test_one_away():
    assert chapter1.one_away('pale', 'ple') == True
    assert chapter1.one_away('pales', 'pale') == True
    assert chapter1.one_away('pale', 'bale') == True
    assert chapter1.one_away('pale', 'bake') == False


def test_string_compression():
    assert chapter1.string_compression('aabcccccaaa') == 'a2b1c5a3'
    assert chapter1.string_compression('aabbccaa') == 'aabbccaa'


def _test_rotate_matrix(func):
    assert func([ [1, 2], [3, 4] ]) == [ [2, 4], [1, 3] ]
    assert func([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
         ]) == [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7],
         ]
    assert func([ 
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]) == [
            [4, 8, 12, 16],
            [3, 7, 11, 15],
            [2, 6, 10, 14],
            [1, 5, 9, 13],
        ]


def test_rotate_matrix():
    _test_rotate_matrix(chapter1.rotate_matrix)


def test_rotate_matrix2():
    _test_rotate_matrix(chapter1.rotate_matrix2)


def test_zero_matrix():
    assert chapter1.zero_matrix([ [0, 0, 3], [4, 0, 6], [7, 8, 9] ]) == \
       [[0, 0, 0], [0, 0, 0], [0, 0, 9]]


def test_string_rotation():
    assert chapter1.string_rotation('waterbottle', 'terbottlewa') == True
    assert chapter1.string_rotation('waterbottle', 'terbottleww') == False