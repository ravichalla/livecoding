import single_linked_list_headTail
import unittest

class StartNode:
    def __init__(self,key):
        self.key= key
        self.next= None
if hasattr(single_linked_list_headTail,"Node"):
    nodeClass= single_linked_list_headTail.Node

class Node(nodeClass):
    pass


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        linkedlist = single_linked_list_headTail.LinkedList
        node = Node(1)
        linkedlist.pushFront(self,node)

if __name__ == "__main__":
    unittest.main()