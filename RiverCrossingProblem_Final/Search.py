# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 00:02:03 2019

@author: Taha
"""



#from com.search.node import Node
from RiverCrossingState import RiverCrossingState
from RiverCrossingProblem import RiverCrossingProblem
from strategy.breadthFirstSearchStrategy import BreadthFirstSearchStrategy

class Search(object):
    '''
    classdocs
    '''


    def __init__(self, searchProblem, searchStrategy):
        '''
        Constructor
        '''
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        
           
    def solveProblem(self):
        currentState=self.searchProblem
  #      explored={}
        stretegy = []
        stretegy.append(currentState)
   #     explored[currentState]=currentState
        while(True):
            node = stretegy.pop(0)
            if(node.is_goal()):
                return node
   #         explored[node]= node
            p = RiverCrossingProblem(self.searchProblem)
            childNodes = p.succesorFunction(node)
            for x in childNodes:
                stretegy.append(x)
            
        return None
    
    
                
    def printPath(self,s):
        if(s is None):
            return 
        self.printPath(s.parent)
        print ("(" + str(s.humanLeft) + "," + str(s.canibalLeft) \
                                  + "," + s.position + "," + str(s.humanRight) + "," + \
                                  str(s.canabilRight) + ")")
    

    	
        
        
        
if __name__=='__main__':
        search = Search(RiverCrossingState(3,3,'Left',0,0),BreadthFirstSearchStrategy())
        solution = search.solveProblem()
        print("(HumanLeft,cannibalLeft,boatPosition,HumanRight,cannibalRight)")
        print(search.printPath(solution))

