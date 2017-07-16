#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 21:23:32 2017

@author: LiryChan
"""

import random

def Begin():
    k = [0, 0, 0, 0, 0]
    for i in range(5):
        k[i] = random.randint(1,3)
        
    for i in range(96):
        print("list", k)
        outcome = game(k)
        # rock=1 paper=2 Scissor=3 
        
        if outcome == [1]:
            name = "rock"
        elif outcome == [2]:
            name = "paper"
        elif outcome == [3]:
            name = "scissor"
        print(name)
        
        k.extend(outcome)
        
def game(ret):     
    if four(ret) == 1:
        return [3]
    elif four(ret) == 2:
        return [1]
    elif four(ret) == 3:
        return [2]
        
        
def four(ret):
    
    tep = ret[:-1]
    for i in range((len(tep)- 4)):
        if ret[-4:] == tep[-5:-1]:
            print("four",tep[-4])
            return tep[-1]
        
        else:
            tep = tep[:-1]           

    return three(ret)

def three(ret):
    tep = ret[:-1]
    for i in range((len(tep)- 3)):
#    while len(tep) > 3:
        if ret[-3:] == tep[-4:-1]:
            print("three",tep[-3])
            return tep[-1]        
        else:
            tep = tep[:-1]

    return two(ret)
            
def two(ret):
    tep = ret[:-1]
    for i in range((len(tep)- 2)):
#    while len(tep) > 2:
        if ret[-2:] == tep[-3:-1]:
            return tep[-1]
            print("two",tep[-2])
        else:
            tep = tep[:-1]
        #While LOOP!!!
    return one(ret)

def one(ret):
    tep = ret[:-1]
    for i in range((len(tep)- 1)):
#    while len(tep) > 1:
        if tep[-1] == tep[-2]:
            return tep[-1]
        else:
            tep = tep[:-1]
    return tep[-1]
            
