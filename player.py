
class Player:
    
    
      
    def __init__(self, strategy):
        
        
        #self.strategy = strategy
        self.old_strategy = strategy
        self.new_strategy = strategy
        self.score = 0 
        self.coloured = False 
        
    
     #this is for the original        
    #def set_strat(self, n_strat):
    #    
    #    self.strategy = n_strat
    #    
    #def get_strat(self):
    #    
    #    return self.strategy 
    
    
    def set_new_strat(self, n_strat):
       
     self.new_strategy = n_strat
      
    def get_new_strat(self):
        
        return self.new_strategy 
        
    def set_old_strat(self, n_strat):
       
     self.old_strategy = n_strat
      
    def get_old_strat(self):
        
        return self.old_strategy 
        
    def get_score(self):
        return self.score
        
    def set_score(self, n_score):
        
        self.score = n_score 
        
    def isColoured(self):
        
        if self.old_strategy >0:    
            self.coloured = True
        
        return self.coloured
        
        
    
        
        
        
        
        
        
        
        
        
        
        