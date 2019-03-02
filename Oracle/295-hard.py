#find median from data stream
from heapq import heappush, heappop, heapreplace, heapify
class MedianFinder(object):

    def __init__(self):
        #keep smaller half (size >= 1)
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return ((-self.maxHeap[0] + self.minHeap[0] + 0.00 )/2)



from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

