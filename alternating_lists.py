#! /usr/bin/env python3

# <<Alternating Lists>>
# <<https://programmingpraxis.com/2019/02/01/alternating-lists/>>

from itertools import zip_longest

def alternate(*lists):
    return [item for tup in zip_longest(*lists) for item in tup
            if item is not None]

def test():
    l1, l2, l3 = [1,2,3,4,5], ["a", "b", "c"], ["w", "x", "y", "z"]
    print(alternate(l1, l2, l3))
    assert alternate(l1, l2, l3) == [1, "a", "w", 2, "b", "x", 3, "c", "y", 4, "z", 5]
