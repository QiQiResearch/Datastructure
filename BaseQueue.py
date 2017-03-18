# -*- coding:utf-8 -*-
class Queue():
    def __init__(self,size):
        self.size = size
        self.content = []

    def LengthQueue(self):
        return len(self.content)

    def EnteranceQueue(self,data):
        if self.LengthQueue() == self.size:
            print "The Queue Is Full!"
        else:
            self.content.append(data)

    def ExitQueue(self):
        if self.LengthQueue() == 0:
            print "The Queue Is Empty!"
        else:
            self.content.pop(0)

    def PrintQueue(self):
        for i in range(0,self.LengthQueue()):
            print self.content[i]

    def IsEmptyQueue(self):
        return self.content == []

    def ClearQueue(self):
        self.content = []

    def DestoryQueue(self):
        self.size = 0


if __name__ == '__main__':
    queue = Queue(20)
    for i in range(2,6):
        queue.EnteranceQueue(i)
    print "第一次打印："
    queue.PrintQueue()
    queue.ExitQueue()
    print "第二次打印："
    queue.PrintQueue()
    queue.DestoryQueue()
    # queue.ClearQueue()
    print "第三次打印："
    queue.PrintQueue()
    print queue.IsEmptyQueue()
