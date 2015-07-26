#-*- coding: UTF-8 -*-
'''
Created on 2015

@author: hua
'''

class A(object):
    def __init__(self):
        self.test1=1111
        self.test2=None
        self.test3 = 'test4'
class B(A):
    def test(self):
        print self.test1
        print self.test2

if __name__ == '__main__':
    b = B()
    b.test()
    print b.test1
    print b.test2
    print b.test3