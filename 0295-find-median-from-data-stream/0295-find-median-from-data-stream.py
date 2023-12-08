class MedianFinder:

    def __init__(self):
        self.first = [] #max heap
        self.second = []#min heap

    def addNum(self, num: int) -> None:
        if not self.first or -self.first[0] >= num:
            heappush(self.first, -num)
            
        else:
            heappush(self.second, num)
        
        if len(self.first) > len(self.second)+1:
            heappush(self.second, -heappop(self.first))
        elif len(self.first) < len(self.second):
            heappush(self.first, -heappop(self.second))
                
        

    def findMedian(self) -> float:
        if (len(self.first) + len(self.second)) % 2 == 0:
            return (-self.first[0] + self.second[0])/2
        else:
            return -self.first[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()