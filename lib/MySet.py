class MySet:
    def __init__(self, list=[]):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def __repr__(self):
        return f"Myset({set(self.dictionary.keys())})"

    def has(self, value):
        return value in self.dictionary
    
    def add(self,value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        return self.dictionary.clear()
    
list1 = MySet([1,2,3,4,5])
print(list1.add(6))
print(list1.has(4))
print(list1.delete(9))
print(list1.size())
print(list1.clear())


    


