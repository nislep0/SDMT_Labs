
class Node:
    def __init__(self, data:str) -> None:
        self.data = data
        self.next = None 
        self.prev = None

class DoubleLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        new_node = Node(element)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.append(element)
            return 
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
        self.size += 1
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if index == 0:
            remove_data = self.head.data
            self.head = self.tail.prev
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            remove_data = self.tail.data
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            remove_data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return remove_data

    def deleteAll(self, element: str) -> None:
        current = self.head
        while current:
            if current.data == element:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
            current = current.next   
    
    def get(self, index:int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        new_list = DoubleLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def reverse(self) -> None:
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def findFirst(self, element: str) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        current = self.tail
        index = self.size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1
        
    def clear(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def extend(self, elements) -> None:
        current = elements.head
        while current:
            self.append(current.data)
            current = current.next
