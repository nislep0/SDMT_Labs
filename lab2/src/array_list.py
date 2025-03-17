class ArrayList:
    def __init__(self):
        self.data = []

    def length(self) -> int:
        return len(self.data)
    
    def append(self, element: str) -> None:
        self.data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        self.data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        return self.data.pop(index)

    def deleteAll(self, element: str) -> None:
        self.data = [x for x in self.data if x != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        return self.data[index]

    def clone(self) -> 'ArrayList':
        new_list = ArrayList()
        new_list.data = self.data.copy()
        return new_list

    def reverse(self) -> None:
        self.data.reverse()

    def findFirst(self, element: str) -> int:
        try: 
            return self.data.index(element)
        except ValueError:
            return -1

    def findLast(self,element: str) -> int:
        try: 
            return self.length() -1 - self.data[::-1].index(element)
        except ValueError:
            return -1

    def clear(self) -> None:
        self.data.clear()

    def extend(self, elements: 'ArrayList') -> None:
        self.data.extend(elements.data.copy())