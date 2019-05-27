# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:51:33 2019

@author: Taha
"""


from searchProblem import SearchProblem
from RiverCrossingState import RiverCrossingState

class RiverCrossingProblem(SearchProblem):
    '''
    classdocs
    '''

    def __init__(self, initialState):
        '''
        Constructor
        '''
        self._initialState = initialState 
        
    def initialState(self):
        return self._initialState
    
    def succesorFunction(self,currentState):
        self.visitedList=[]
        self.visitedList.append(currentState)
        #Actions : Left , Right
        #Assuming Initial State (3,3,Left,0,0)
        #Constrains = Canable Should not outlimit Human
        
        nextMoves=[]
        
        if currentState.position=='Left': 
            newNode_1H_1C = RiverCrossingState(currentState.humanLeft-1,currentState.canibalLeft-1,'Right',currentState.humanRight+1,currentState.canabilRight+1)
            newNode_2H = RiverCrossingState(currentState.humanLeft-2,currentState.canibalLeft,'Right',currentState.humanRight+2,currentState.canabilRight)
            newNode_2C = RiverCrossingState(currentState.humanLeft,currentState.canibalLeft-2,'Right',currentState.humanRight,currentState.canabilRight+2)
            newNode_1H = RiverCrossingState(currentState.humanLeft-1,currentState.canibalLeft,'Right',currentState.humanRight+1,currentState.canibalLeft)
            newNode_1C = RiverCrossingState(currentState.humanLeft,currentState.canibalLeft-1,'Right',currentState.humanRight,currentState.canabilRight+1)
               
                # Canables should be less than humans on either side or there should be no human on the side .
            if  self.positiveValue(newNode_1H_1C) and (newNode_1H_1C.canibalLeft <= newNode_1H_1C.humanLeft  or newNode_1H_1C.humanLeft==0)   and (newNode_1H_1C.canabilRight <= newNode_1H_1C.humanRight or newNode_1H_1C.humanRight == 0 ):
                newNode_1H_1C.parent=currentState
                nextMoves.append(newNode_1H_1C)
            if self.positiveValue(newNode_2H) and (newNode_2H.canibalLeft <= newNode_2H.humanLeft   or newNode_2H.humanLeft==0)  and  (newNode_2H.canabilRight <= newNode_2H.humanRight or newNode_2H.humanRight == 0 ):
                newNode_2H.parent=currentState
                nextMoves.append(newNode_2H)
            if self.positiveValue(newNode_2C) and (newNode_2C.canibalLeft <= newNode_2C.humanLeft   or newNode_2C.humanLeft==0 ) and (newNode_2C.canabilRight <= newNode_2C.humanRight or newNode_2C.humanRight == 0) :
                newNode_2C.parent=currentState
                nextMoves.append(newNode_2C)
            if self.positiveValue(newNode_1H) and (newNode_1H.canibalLeft <= newNode_1H.humanLeft   or newNode_1H.humanLeft==0 ) and (newNode_1H.canabilRight <= newNode_1H.humanRight or newNode_1H.humanRight == 0 ):
                newNode_1H.parent=currentState
                nextMoves.append(newNode_1H)
            if self.positiveValue(newNode_1C) and (newNode_1C.canibalLeft <= newNode_1C.humanLeft   or newNode_1C.humanLeft==0 ) and (newNode_1C.canabilRight <= newNode_1C.humanRight or newNode_1C.humanRight == 0 ):
                newNode_1C.parent=currentState
                nextMoves.append(newNode_1C)
        else: 
            newNode_1H_1C = RiverCrossingState(currentState.humanLeft+1,currentState.canibalLeft+1,'Left',currentState.humanRight-1,currentState.canabilRight-1)
            newNode_2H = RiverCrossingState(currentState.humanLeft+2,currentState.canibalLeft,'Left',currentState.humanRight-2,currentState.canabilRight)
            newNode_2C = RiverCrossingState(currentState.humanLeft,currentState.canibalLeft+2,'Left',currentState.humanRight,currentState.canabilRight-2)
            newNode_1H = RiverCrossingState(currentState.humanLeft+1,currentState.canibalLeft,'Left',currentState.humanRight-1,currentState.canabilRight)
            newNode_1C = RiverCrossingState(currentState.humanLeft,currentState.canibalLeft+1,'Left',currentState.humanRight,currentState.canabilRight-1)
               
            if  self.positiveValue(newNode_1H_1C) and ( newNode_1H_1C.canibalLeft <= newNode_1H_1C.humanLeft   or newNode_1H_1C.humanLeft==0)  and (newNode_1H_1C.canabilRight <= newNode_1H_1C.humanRight or newNode_1H_1C.humanRight == 0) :
                newNode_1H_1C.parent=currentState
                nextMoves.append(newNode_1H_1C)
            if self.positiveValue(newNode_2H) and (newNode_2H.canibalLeft <= newNode_2H.humanLeft   or newNode_2H.humanLeft==0 ) and (newNode_2H.canabilRight <= newNode_2H.humanRight or newNode_2H.humanRight == 0 ):
                newNode_2H.parent=currentState
                nextMoves.append(newNode_2H)
            if self.positiveValue(newNode_2C) and (newNode_2C.canibalLeft <= newNode_2C.humanLeft   or newNode_2C.humanLeft==0)  and (newNode_2C.canabilRight <= newNode_2C.humanRight or newNode_2C.humanRight == 0) :
                newNode_2C.parent=currentState
                nextMoves.append(newNode_2C)
            if self.positiveValue(newNode_1H) and (newNode_1H.canibalLeft <= newNode_1H.humanLeft   or newNode_1H.humanLeft==0 ) and (newNode_1H.canabilRight <= newNode_1H.humanRight or newNode_1H.humanRight == 0) :
                newNode_1H.parent=currentState
                nextMoves.append(newNode_1H)
            if self.positiveValue(newNode_1C) and (newNode_1C.canibalLeft <= newNode_1C.humanLeft   or newNode_1C.humanLeft==0)  and (newNode_1C.canabilRight <= newNode_1C.humanRight or newNode_1C.humanRight == 0 ):
                newNode_1C.parent=currentState
                nextMoves.append(newNode_1C)
        return nextMoves    
    
    def is_goal(self):
        if self.canibalLeft == 0 and self.humanLeft == 0:
            return True
    		
        else:
            return False
    def positiveValue(self,node):
        return node.humanLeft>= 0 and node.canibalLeft >=0 and  node.humanRight>=0 and node.canabilRight>=0
 