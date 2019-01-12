import heapq
import random

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0
        self.entryFinder = {}       #mapping of items to entries in heap

    def push(pq, item, priority):
        pq.count = pq.count + 1
        entry = [item, priority]
        pq.entryFinder[item] = entry
        heapq.heappush(pq.heap, entry)


    def pop(pq):
        if pq.isEmpty():
            return None
        else:
            while pq:
                item, priority = heapq.heappop(pq.heap)
                return item

    def isEmpty(pq):
        if pq.count == 0:
            return True
        else:
            return False

    def update(pq,item,priority):
        if item in pq.entryFinder and priority <= pq.entryFinder[item]:
            pq.entryFinder[item] = priority
        elif item not in pq.entryFinder:
            pq.push(item, priority)


def PQSort(integerList):
    q = PriorityQueue()
    q.isEmpty()
    priority = 0
    for i in range(0,len(integerList)):
        priority = random.randint(0,100)
        item = integerList[i]
        q.update(item, priority)
        #priority += 1
    for i in range(0, q.count):
        t = q.pop()
        print t



if __name__ == '__main__':
    list = [5,3,1,9,13,8,6,29,7,10,5,0]
    PQSort(list)
