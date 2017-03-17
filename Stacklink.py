# -*-coding:utf-8 -*-
class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Stacklink(object):
    def __init__(self):
        self.head = 0
        self.top = -1

    '''入栈'''
    def PushStacklink(self,data):
        newnode = Node(data)
        p = self.head
        newnode.next = p
        self.head = newnode
        self.top = self.top + 1

    '''出栈'''
    def PopStacklink(self):
        p = self.head
        self.head = p.next
        self.top = self.top - 1

    '''打印栈中的数据'''
    def PrintStacklink(self):
        p = self.head
        temp = self.top
        while self.top != -1:
            print p.data
            p = p.next
            self.top = self.top - 1

        self.top = temp


if __name__ == '__main__':
    Stacklink = Stacklink()
    for i in range(1,10):
        Stacklink.PushStacklink(i)
    print "栈的内容："
    Stacklink.PrintStacklink()
    for i in range(1,4):
        Stacklink.PopStacklink()
    print "栈的内容："
    Stacklink.PrintStacklink()