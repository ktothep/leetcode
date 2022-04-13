class MedianFinder:

    def __init__(self):
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)%2!=0:
            return self.arr[len(self.arr)//2]
        else:
            mid=len(self.arr)//2-1
            x=self.arr[mid]
            y = self.arr[mid+1]
            return (x+y)/2


obj=MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
print(obj.findMedian())

