# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:38:31 2016

@author: eikes
"""
import io
import sys

from chapter2 import Node, remove_dups, k_to_end


class CaptureStdout(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def test_remove_dups():
    n7 = Node(0)
    n6 = Node(1, n7)
    n5 = Node(3, n6)
    n4 = Node(4, n5)
    n3 = Node(0, n4)
    n2 = Node(0, n3)
    n1 = Node(1, n2)
    root = Node(0, n1)
    
    # [0, 1, 0, 0, 4, 3, 1, 0]
    assert str(root) == '[ 0, 1, 0, 0, 4, 3, 1, 0 ]'
    remove_dups(root)
    # [0, 1, 4, 3]
    assert str(root) == '[ 0, 1, 4, 3 ]'
    
def test_k_to_end():
    n7 = Node(0)
    n6 = Node(1, n7)
    n5 = Node(3, n6)
    n4 = Node(4, n5)
    n3 = Node(0, n4)
    n2 = Node(0, n3)
    n1 = Node(1, n2)
    root = Node(0, n1)
    
    with CaptureStdout() as out:
        k_to_end(root, 1)
    assert out[0] == '[ 0 ]'
    
    with CaptureStdout() as out:
        k_to_end(root, 2)
    assert out[0] == '[ 1, 0 ]'
    
    with CaptureStdout() as out:
        k_to_end(root, 3)
    assert out[0] == '[ 3, 1, 0 ]'
    
    with CaptureStdout() as out:
        k_to_end(root, 4)
    assert out[0] == '[ 4, 3, 1, 0 ]'
