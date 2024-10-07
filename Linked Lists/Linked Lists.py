# Time Complexity for Node Class is O(1)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
# new_node = Node(10)
# print(new_node)

# Time Complexity of Creating a Linked List with one Node is O(1)
class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
# Time Complexity of Creating an empty Linked List is O(1)   
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # Showing Linked List in str
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    # Insert an Element at the end of Linked List
    # Time Complexity is O(1)
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
    
    # Insert an Element at the beginning of Linked List
    # Time Complexity is O(1)
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
    #Insert Element at any index of linked List
    # Time Complexity is O(n)
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0:
            index = self.length + index + 1    
        if index > self.length:
            index = self.length   
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:      
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    # Traversal of Linked List
    # Time Complexity is O(n)
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
    
    # Search Method in Linked List
    # Time Complexity is O(n)
    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return "This Element Does not exists"
    
    # Get Method 
    # Time Complexity is O(n)
    def get(self, index):
        if index < 0:
            index = self.length + index + 1
        if index > self.length:
            index = self.length
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    
    # Set Method(used to update the value of Node based on its index)
    # Time Complexity is O(n)
    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node is not None:
            temp_node.value = value
            return True
        return False
    
    # Pop first Method
    # Time Complexity is O(1)
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    # Pop first Method
    # Time Complexity is O(n)
    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.length -= 1
            return popped_node
        
    # Remove Method
    # Time Complexity is O(n)
    def remove(self,index):
        if index < 0:
            index = self.length + index
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    # Delete All Nodes of Linked List
    # Time Complexity is O(1)
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

    



    


         


        

 






        




new_linked_list = LinkedList()
# Insert an Element at the end of Linked List
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
print(new_linked_list)
# Insert an Element at the beginning of Linked List
new_linked_list.prepend(30)
print(new_linked_list)
#Insert Element at any index of linked List
new_linked_list.insert(0,40)
new_linked_list.insert(-2,50)
print(new_linked_list)
# Traversal of Linked List
new_linked_list.traverse()
# Searching in Linked List
print(new_linked_list.search(50))
print(new_linked_list.search(60))
print(new_linked_list.get(-1).value)
print(new_linked_list.set_value(2,90))
print(new_linked_list)
new_linked_list.pop_first()
print(new_linked_list)
new_linked_list.pop()
print(new_linked_list)
new_linked_list.remove(2)
print(new_linked_list)
print(new_linked_list.tail.value)
new_linked_list.delete_all()
print(new_linked_list)