'''
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def get(self, index: int) -> int:
        if index >= self.count:
            return -1
        
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            
            cur = cur.next
            i += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        if not self.tail:
            self.tail = new_head
        self.count += 1

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if not self.head:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        self.count += 1

    def remove(self, index: int) -> bool:
        if index >= self.count:
            return False
        if index == 0:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.count -= 1
            return True
        
        i = 0
        cur = self.head
        while cur:
            if (i + 1) == index:
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
                self.count -= 1
                return True
            cur = cur.next
            i += 1
        
        return False

    def getValues(self) -> list[int]:
        values = []
        cur = self.head

        while cur:
            values.append(cur.val)
            cur = cur.next
        return values