# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:59:48 2019

@author: Taha
"""

class RiverCrossingState():
    def __init__(self,humanL,canibalL,position,humanR,canabilR,parent=None):
        self.humanLeft=humanL
        self.canibalLeft=canibalL
        self.position=position
        self.humanRight=humanR
        self.canabilRight= canabilR
        self.parent = None 

    def is_goal(self):
        if self.canibalLeft == 0 and self.humanLeft == 0:
            return True
    		
        else:
            return False


  