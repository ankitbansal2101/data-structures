#double ended queue

import collections

DoubleEnded = collections.deque(["Mon","Tue","Wed"])

DoubleEnded.append("Thu")

print ("Appended at right - ")
print (DoubleEnded)

DoubleEnded.appendleft("Sun")

print ("Appended at right at left is - ")
print (DoubleEnded)

DoubleEnded.pop()

print ("Deleting from right - ")
print (DoubleEnded)

DoubleEnded.popleft()

print ("Deleting from left - ")
print (DoubleEnded)



class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)