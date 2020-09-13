import program
import unittest

class StartLinkedList:
    def __init__(self,value):
        self.value= value
        self.next= None
linkedListClass = StartLinkedList

if hasattr(program, "LinkedList"):
    linkedListClass = program.LinkedList

class LinkedList(linkedListClass):
    def addMany(self,values):
        current= self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
    def getNodesInArray(self):
        nodes=[]
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

class TestProgram(unittest.TestCase):
    def test_case_9(self):
        test9 = LinkedList(0).addMany([1,2,3,4,5,6,7,8,9])
        result9 = LinkedList(0).addMany([2,3,4,5,6,7,8,9])
        program.removeKthNodeFromEnd(test9,9)
        self.assertEqual(test9.getNodesInArray(), result9.getNodesInArray())
    def test_case_10(self):
        test10 = LinkedList(0).addMany([1,2,3,4,5,6,7,8,9])
        result10 = LinkedList(1).addMany([2,3,4,5,6,7,8,9])
        program.removeKthNodeFromEnd(test10,10)
        self.assertEqual(test10.getNodesInArray(), result10.getNodesInArray())