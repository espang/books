# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:27:21 2016

my solution to tasks from the book: 'Cracking the coding interview'

@author: espang
"""
import collections

import numpy as np


def is_unique(s):
    '''
    checks if s (string) has no duplicated letters
    returns True if so, False otherwise
    '''
    occured_letters = set(s)
    return len(s) == len(occured_letters)


def is_permutation(s1, s2):
    '''
    checks wether s2 is a permutation of s1
    returns True if it is a permutation, False otherwise
    '''
    #necessary condition: same amount of letters
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def urlify(url, last_index):
    #just works for strings
    assert type(url) == str
    url_array = bytearray(url, 'utf-8')
    
    insert_index = len(url) - 1
    
    space, zero, two, percent = ord(' '), ord('0'), ord('2'), ord('%')
    for i in range(last_index-1, -1, -1):
        if not url_array[i] == space:
            # it is not a space -> copy value
            url_array[insert_index] = url_array[i]
            insert_index -= 1
        else:
            # it is a space -> replace
            url_array[insert_index] = zero
            url_array[insert_index-1] = two
            url_array[insert_index-2] = percent
            insert_index -= 3
    return url_array.decode()


def is_permutation_of_palindrom(s):
    '''
    checks if a palindrom exists with the letters of s
    return True if a palindrom exists, False otherwise
    '''
    counter = collections.Counter()
    for c in s:
        if c == ' ':
            continue
        counter[c] += 1
    # when all letters have even counts there could be a palindrom
    # otherwise there could be a palindrom when there is just 1 letter
    #  with an odd count (cause the length of the string would be odd too) 
    found_an_odd = False
    for _, c in counter.items():
        if c % 2 == 1:
            if found_an_odd:
                # two odds -> no palindrom!
                return False
            found_an_odd = True
    return True    


def _one_away_remove(s1, s2):
    '''
        s1 has one letter more than s2    
    '''
    addend = 0
    for idx, c2 in enumerate(s2):
        c1 = s1[idx+addend]
        if c1 != c2:
            if addend == 1:
                return False
            addend = 1
    return True


def one_away(s1, s2):
    '''
    three possible actions on one string:
    * insert, remove or replace a single char
      (insert in the smaller is equivalent to removing in the larger string)
    return True if strings are equal with zero or one action, False otherwise    
    '''
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        changed_one = False
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if changed_one:
                    return False
                changed_one = True
        return True
    if len(s1) == len(s2) + 1:
        return _one_away_remove(s1, s2)
    if len(s1) + 1 == len(s2):
        return _one_away_remove(s2, s1)
    return False


def string_compression(s):
    '''
     compress 'aabcccccaaa' to 'a2b1c5a3'
     return the compressed string if the length is shorter, the original string
            otherwise
    '''
    if len(s) == 0:
        return s
    arr = []
    last_letter = s[0]
    count = 1
    for c in s[1:]:
        if c != last_letter:
            arr.append('%s%d' % (last_letter, count))
            last_letter = c
            count = 1
            continue
        count += 1
    else:
        #add the last
        arr.append('%s%d' % (last_letter, count))
    result = ''.join(arr)
    return result if len(result) < len(s) else s


def rotate_matrix(d):
    '''
    return rotated matrix d
    '''
    n = len(d)
    
    for row in range(0, n//2):
        for col in range(row, n-1-row):
            d[n-1-col][row], save = d[row][col], d[n-1-col][row]
            d[n-1-row][n-1-col], save = save, d[n-1-row][n-1-col]
            d[col][n-1-row], save = save, d[col][n-1-row]
            d[row][col] = save
    return d


def rotate_matrix2(d):
    '''
     as rotate_matrix but with numpy
    '''
    _mat = np.matrix(d)
    cols, _ = _mat.shape
    #swap columns and transpose matrix rotates the matrix
    return _mat[:, np.arange(cols-1, -1, step=-1)].T.tolist()


def zero_matrix(mat):
    '''
    if a element is zero: set row and column to zero
    '''
    _mat = np.matrix(mat)

    #search zeros    
    cols = set()
    rows = set()
    for col, row in np.argwhere(_mat==0):
        cols.add(col)
        rows.add(row)
    
    #remove zeros
    for col in cols:
        _mat[:, col] = 0
    for row in rows:
        _mat[row, :] = 0

    return _mat.tolist()


def string_rotation(s1, s2):
    '''
    example: 
     "waterbottle" is a rotation of "terbottlewa"
    '''
    # waterbottlewaterbottle contains any rotation like terbottlewa
    idx = (s1+s1).find(s2)
    # idx is -1 if s2 not in s1s1
    return idx != -1
    