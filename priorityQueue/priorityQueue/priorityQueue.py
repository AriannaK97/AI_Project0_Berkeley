import heapq
import random

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.entryFinder = {}       #mapping of items to entries in heap using a dictionary

    def push(self, item, priority):
        self.count = self.count + 1             #increase the count of the queue
        entry = [priority, self.count, item]    #create the entry, each queue entry is a list of two items, the item we want to store and the priority
        self.entryFinder[item] = entry
        heapq.heappush(self.heap, entry)


    def pop(self):
        if self.isEmpty():
            return None
        else:
            while self:
                #the heappop function returns all these three values we have stored
                priority, count, item = heapq.heappop(self.heap)
                return item


    def isEmpty(self):
        #if the list is empty the counter is 0
        if self.count == 0:
            return True
        else:
            return False


#in contrast to push function, the update one does not keep duplicate items
    def update(self,item,priority):
        #in case the priority of the new entry is smaller than the priority of the existing one in the queue and the dictionary
        if item in self.entryFinder and priority <= self.entryFinder[item]:
            self.entryFinder[item] = priority
        #any other case
        elif item not in self.entryFinder:
            self.push(item, priority)


def PQSort(integerList):
    q = PriorityQueue()
    sortedList = []
    priority = 0
    for i in range(0,len(integerList)):
        item = integerList[i]
        priority = item
        q.push(item, priority)
    #creating the sorted list
    for i in range(0, q.count):
        t = q.pop()
        sortedList.append(t)
    return sortedList



if __name__ == '__main__':
    sortedList = []
    integerList = [5,3,1,9,13,8,6,29,7,10,5,0]
    sortedList = PQSort(integerList)
    #printing the sorted list
    print "The list has been sorted\n", sortedList
