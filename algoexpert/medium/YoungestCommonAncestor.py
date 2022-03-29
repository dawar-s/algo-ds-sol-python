# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor: AncestralTree, descendantOne: AncestralTree, descendantTwo: AncestralTree):
    h1, h2 = 0, 0
    d1, d2 = descendantOne, descendantTwo
    while d1 is not None:
        h1 += 1
        d1 = d1.ancestor
    while d2 is not None:
        h2 += 1
        d2 = d2.ancestor

    if h1 != h2:
        if h1 > h2:
            while h1 != h2:
                descendantOne = descendantOne.ancestor
                h1 -= 1
        else:
            while h1 != h2:
                descendantTwo = descendantTwo.ancestor
                h2 -= 1

    while descendantOne is not descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    return descendantOne