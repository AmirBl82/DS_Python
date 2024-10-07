# Time Complexity for Node Class is O(1)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

# Time Complexity of Creating a Circular Linked List with one Node is O(1)
class Circular_linkedList:
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

# Time Complexity of Creating an empty Circular Linked List is O(1)   
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Showing Circular Linked List in str
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    # Insert an Element at the end of Circular Linked List
    # Time Complexity is O(1)
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    # Insert an Element at the beginning of Circular Linked List
    # Time Complexity is O(1)
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
    # Insert an Element at any given index in Circular Linked List
    # Time Complexity is O(n)
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0:
            index = self.length + index + 1
        if index > self.length:
            index = self.length
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head 
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    # Traversal of Circular Linked List
    # Time Complexity is O(n)
    def traverse(self):
        if not self.head:  # If the list is empty
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
    

    # Searching for an Element in Circular Singly Linked List
    # Time Complexity is O(n)
    def search(self, target):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target:
                return "Element Found"
            current_node = current_node.next
            if current_node == self.head:
                break
        return "Element not Found"
    
    # Get Method in Circular Linked List
    # Time Complexity is O(n)
    def get(self, index):
        if index < 0:
            index = self.length + index
        if index > self.length:
            index = self.length
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    # Set Method in Circular Linked List
    # Time Complexity is O(n)
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    # Pop first Method
    # Time Complexity is O(1)
    def pop_first(self):
        popped_Node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.head = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_Node.next = None
        self.length -= 1
        return popped_Node



    





CLinkedList = Circular_linkedList()
CLinkedList.append(10)
CLinkedList.append(20)
print(CLinkedList.head.value)
print(CLinkedList.tail.value)
print(CLinkedList)
CLinkedList.prepend(40)
print(CLinkedList)
CLinkedList.prepend(50)
print(CLinkedList)
CLinkedList.insert(0, 30)
print(CLinkedList)
CLinkedList.insert(-1, 60)
print(CLinkedList.tail.value)
print(CLinkedList)
print(CLinkedList.traverse())
print(CLinkedList.search(60))
print(CLinkedList.search(70))
print(CLinkedList.get(-1))
print(CLinkedList.set_value(-2, 100))
print(CLinkedList)
print(CLinkedList.get(-5))
print(CLinkedList.pop_first())
print(CLinkedList)