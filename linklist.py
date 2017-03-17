# -*-coding:utf-8 -*-
class Node(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class linklist(object):
    '''初始化空链表'''
    def __init__(self):
        self.head = 0

    '''创建一个新链表'''
    def Initiallist(self,data):
        if len(data) == 1:
            self.head = Node(data[0])
        else:
            self.head = Node(data[0])
            p = self.head
            for i in data[1:]:
                p.next = Node(i)
                p = p.next
        return

    '''判断链表是否为空'''
    def IsEmptylist(self):
        return self.head == 0

    '''打印链表'''
    def Printlist(self):
        if self.IsEmptylist():
            print "Linklist Is Empty!"
        else:
            p = self.head
            while p!= None:
                print p.data
                p = p.next

    '''链表长度'''
    def Lengthlist(self):
        length = 0
        p = self.head
        while p!= None:
            p = p.next
            length = length + 1
        return length

    '''链表长度'''
    def Clearlist(self):
        self.head = 0

    '''在链表的指定位置插入元素'''
    def Insertlist(self,data,Index):
        if Index < 0 or Index > self.Lengthlist():
            print "The Index Is Wrong!"
        # 在链表头部插入元素
        elif Index == 0:
            newnode = Node(data)
            p = self.head
            newnode.next = p
            self.head = newnode
        # 在链表尾部插入元素
        elif Index == self.Lengthlist():
            p = self.head
            newnode = Node(data)
            i = 1
            while i < Index:
                p = p.next
                i = i + 1
            p.next = newnode
        # 在链表中间插入元素
        else:
            i = 1
            p = self.head
            newnode = Node(data)
            while i < Index:
                p = p.next
                i = i + 1
            newnode.next = p.next
            p.next = newnode

    '''在链表的指定位置删除元素'''
    def Deletelist(self,Index):
        if Index < 0 or Index > self.Lengthlist()-1:
            print "The Index Is Wrong!"
        # 删除链表的头元素
        if Index == 0:
            p = self.head
            self.head = p.next

        # 删除链表的尾元素
        elif Index == self.Lengthlist()-1:
            i = 1
            p = self.head
            while i < Index:
                p = p.next
                i = i + 1
            p.next = None

        #删除链表的中间元素
        else:
            i = 1
            p = self.head
            while i < Index:
                p = p.next
                i = i + 1
            p.next = p.next.next

    '''获取链表指定位置的元素'''
    def GetElemlist(self,Index):
        if Index == 0:
            p = self.head
        else:
            p = self.head
            i = 0
            while i < Index:
                p = p.next
                i = i + 1
        return p.data

if __name__ == '__main__':
    Linklist = linklist()
    Linklist.Initiallist([1,2,3,4,5,67,8])
    print "链表长度：",Linklist.Lengthlist()
    print "链表的第一个元素:",Linklist.GetElemlist(6)
    print "插入元素后的数组"
    Linklist.Insertlist(5,7)
    print "第1次——打印链表："
    Linklist.Printlist()
    print "删除元素后的数组"
    Linklist.Deletelist(6)
    print "第2次——打印链表："
    Linklist.Printlist()
    print "清空链表"
    Linklist.Clearlist()
    print "第3次——打印链表："
    Linklist.Printlist()


