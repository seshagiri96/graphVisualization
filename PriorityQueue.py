class BinHeap:
    def __init__(self):
        self.heapList = [[0,-1]]
        self.currentSize = 0

    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i][1] < self.heapList[i//2][1]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i//2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][1] > self.heapList[mc][1]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if 2*i+1 > self.currentSize:
            return 2*i
        else:
            if self.heapList[2*i][1] < self.heapList[2*i+1][1]:
                return 2*i
            else:
                return 2*i+1

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [[0,0]] + alist[:]
        while(i > 0):
            self.percDown(i)
            i = i-1

    def delMin(self):
        retval = self.heapList[1][0]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 0

    def editPriority(self,ob):
        for i in range(1,self.currentSize+1):
            if self.heapList[i][0] == ob[0]:
                self.heapList[i] = ob
                self.percUp(i)
                break
    def check(self,i):
        for j in range(1,self.currentSize+1):
            if i == self.heapList[j][0]:
                return 1
        return 0