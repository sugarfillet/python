#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Shaw Song'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

'''
abc        public
__xxx__    可以被直接引用 但有特殊用途
_xxx __xxx private 不应该被直接引用
'''


