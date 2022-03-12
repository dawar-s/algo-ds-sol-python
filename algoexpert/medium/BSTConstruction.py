class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        parent = None

        while current is not None:
            parent = current
            if current.value > value:
                current = current.left
            else:
                current = current.right
        if parent.value > value:
            parent.left = BST(value)
        else:
            parent.right = BST(value)
        return self

    def contains(self, value):
        current = self
        while current is not None:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False

    def remove(self, value):
        # if there is only root node
        if self.__isleafnode__():
            return self

        current = self
        parent = None
        while current is not None and current.value != value:
            parent = current
            if current.value > value:
                current = current.left
            else:
                current = current.right

        if current is not None and current.value == value:
            if current.__isleafnode__():
                if parent.value > value:
                    parent.left = None
                else:
                    parent.right = None
            elif current.__hastwochildren__():
                smallestnode, smallestnodeparent = current.__getsmallestnode__()
                current.value = smallestnode.value
                if smallestnodeparent is None:
                    current.right = None
                else:
                    smallestnodeparent.left = None
            else:
                if parent is None:
                    if current.right is None:
                        self.value = current.left.value
                        self.left = current.left.left
                    else:
                        smallestnode, smallestnodeparent = self.__getsmallestnode__()
                        self.value = smallestnode.value
                        if smallestnodeparent is None:
                            self.right = smallestnode.right
                            smallestnode = None
                        else:
                            smallestnodeparent.left = None
                elif parent.value <= current.value:
                    if current.left is not None:
                        parent.right = current.left
                        current.left = None
                    else:
                        parent.right = current.right
                        current.right = None
                else:
                    if current.left is not None:
                        parent.left = current.left
                        current.left = None
                    else:
                        parent.left = current.right
                        current.right = None
        print(self)
        return self


    def __isleafnode__(self):
        return self.left is None and self.right is None


    def  __hastwochildren__(self):
        return self.left is not None and self.right is not None


    def __getsmallestnode__(self):
        current = self.right
        parent = None
        while current.left is not None:
            parent = current
            current = current.left
        return current, parent



class TestProgram:
    def test_case_1(self):
        root = BST(10)
        root.insert(5)
        root.remove(10)
        print(root.value)


TestProgram().test_case_1()
