import numpy as np

class Player:
    
    
      
    def __init__(self, strategy, single):
        
        
        #self.strategy = strategy
        self.old_strategy = strategy
        self.new_strategy = strategy
        self.score = 0 
        self.coloured = False 
        self.single = single
    
    
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
        
    def is_coloured_single(self):
        
        if self.old_strategy >0:    
            self.coloured = True
        
        return self.coloured
    
    def is_coloured_double(self):
        
        if np.sum(np.asarray(self.old_strategy)) >0:    
            self.coloured = True
        
        return self.coloured