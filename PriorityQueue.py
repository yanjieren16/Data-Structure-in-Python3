class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def add(self, item):
        self.items.append(item)

    def remove(self):
        # maxi holds the item with top priority
        maxi = 0
        for i in range(1, len(self.items)):
            # compares ith element with current maxi
            # if new item is larger, then set maxi to i
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

# for > operator to compare object type. __gt__method is used to.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.grade)

    # Student with worst grade gets highest priority
    def __gt__(self, other):
        return self.grade < other.grade


# test case
Rob = Student("Ron Weasley", 60)
Link = Student("Hermione Granger", 90)
Arthur = Student("Harry Potter", 70)

pq = PriorityQueue()
for s in [Rob, Link, Arthur]:
    pq.add(s)

while not pq.is_empty():
    print(pq.remove())
