import Vertex


class Graph:
    
    
    def __init__(self):
        
        self.VertList = {}
        self.numVert = 0
        
    
    def addVertex(self, key):
        
        self.numVert +=1
        newVert = Vertex.Vertex(key)
        self.VertList[key] = newVert
        return newVert
        
    def getVertex(self,n):
        
        if n in self.VertList:
            return self.VertList[n]
            
        else: 
            return None
            
    def __contains__(self,n):
         
          return n in self.VertList
          
    def addEdge(self, f,t, cost=0):
        
        if f not in self.VertList:
            
            nv = self.addVertex(f)
            
        if t not in self.VertList:
            
            nv = self.addVertex(t)
            
        self.VertList[f].addNbr(self.VertList[t],cost)
        self.VertList[t].addNbr(self.VertList[f],cost)    
        
    def getVertices(self):
        
        return self.VertList.keys()
        
        
    def __iter__(self):
        return iter(self.VertList.values())
