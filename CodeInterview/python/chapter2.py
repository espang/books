# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:08:27 2016

@author: eikes
"""

class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None

    def __repr__(self):
        vals = []
        i = self
        while i.has_next():
            vals.append(i.value)
            i = i.next_node
        vals.append(i.value)
        return '[ {0} ]'.format(', '.join(map(str, vals)))
        
def remove_dups(node):
    current, last = node, None
    values = set()
    while current is not None:
        if current.value in values:
            #value allready in linked list --> remove current
            last.next_node = current.next_node
        else:
            values.add(current.value)
            last = current
        current = current.next_node

def k_to_end(node, k):
    if not node.has_next():
        if k == 1:
            print (node)
        return 1
    idx = k_to_end(node.next_node, k) + 1
    if idx == k:
        print(node)
    return idx