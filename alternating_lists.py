#! /usr/bin/env python3

# <<Alternating Lists>>
# <<https://programmingpraxis.com/2019/02/01/alternating-lists/>>

def alternate(*lists):
    pass



def test():
    assert alternate([1,2,3,4,5], ["a", "b", "c"], ["w", "x", "y", "z"]) ==
    [1, "a", "w", 2, "b", "x", 3, "c", "y", 4, "z", 5]
