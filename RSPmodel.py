
import player as pl 
import numpy as np 
import RPSboard 

  
class RSPmodel:
    
    def __init__(self):
           self.R = 1
           self.S = 2
           self.P = 3 
           
        
        
    def get_player_n(self,p_coords, grd_sz):
        
        N_coords = []
        
        N_coords.append([p_coords[0]+1,p_coords[1]])
        N_coords.append([p_coords[0]-1,p_coords[1]])
        N_coords.append([p_coords[0]-1,p_coords[1]-1])
        N_coords.append([p_coords[0],p_coords[1]+1])
        N_coords.append([p_coords[0],p_coords[1]-1])
        N_coords.append([p_coords[0]-1,p_coords[1]+1])
        N_coords.append([p_coords[0]+1,p_coords[1]-1])
        N_coords.append([p_coords[0]+1,p_coords[1]+1])
        
        for n_coords in N_coords: 
            for pos in n_coords: 
                if pos <=grd_sz and pos >=1:
                    
                    pos = pos
                
                else: 
                    pos = abs(pos-grd_sz)
                    
        return N_coords 
    
    def get_n_values(self, n_coords, grid):
        
        N_values = []
        
        for cords in n_coords:
            N_values.append(grid[cords[0]-1][cords[1]-1])
        
        return N_values  
        
        
        
        
        
        
    def play(self,player,neighbours):
        
        p_strat = player.get_strat
        
        
        
        
        
        
        
        
        
        
          
        
    
                    
                    
                    
        
        
        
        
        
                
                
                
                 
                    
                
        
        
        
              