# -*- coding:utf-8 -*-
# 20170316 16:04 栈的实现
class stack():
    def __init__(self,size,top = -1):
        self.size = size
        self.stack = []
        self.top = top

    def PushStack(self,data):
        if self.top == self.size - 1:
            print "Stack Is Full!"
        else:
            self.top = self.top + 1
            self.stack.append(data)

    def PopStack(self):
        if self.top == -1:
            print "Stack Is Empty!"
        else:
            self.top = self.top - 1
            self.stack.pop()

    def IsEmptyStack(self):
        return self.top == -1


    def IsFullStack(self):
        return self.top == self.size - 1

    def PrintStack(self):
        return self.stack


if __name__ == '__main__':
     s = stack(20)
     for i in range(3):
         s.PushStack(i)
     print "Stack:",s.PrintStack()
     s.PopStack()
     print "Stack:",s.PrintStack()
     print "Is Stack Empty?:",s.IsEmptyStack()
