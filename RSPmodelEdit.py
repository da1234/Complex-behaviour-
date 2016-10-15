
import player as pl 
import numpy as np 
import RPSboard

  
class RSPmodel:
    
    def __init__(self, no_strats):
           self.R = 1
           self.S = 2
           self.P = 3 
           self.no_strats = no_strats
        
        
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
                    
                    pass
                
                else: 
                    pos = abs(pos-grd_sz)
                    
        return N_coords 
    
    def get_n_values(self, n_coords, grid):
        
        N_values = []
        
        for cords in n_coords:
            N_values.append(grid[cords[0]-1][cords[1]-1])
        
        return N_values  
        
        
        
        
        
        
    def play(self,player,neighbours):
        
        p_strat = player.get_strat()
        current_score = player.get_score()
        
        n_strats = []
        number_of_strats = RSPmodel.no_strats()
        
        for neighbour in neighbours:
            n_strats.append(neighbour.get_strat())
            
        for strat in n_strats:
            if p_strat == strat or abs(p_strat - strat) >= 2:
                    pass
                    
            elif strat == number_of_strats:
                if p_strat == strat - 1:
                    p_strat.set_score(current_score-1)
                elif p_strat == 1:
                    p_strat.set_score(current_score+1)
                    
            elif strat == 1:
                if p_strat == number_of_strats:
                    p_strat.set_score(current_score-1)
                elif p_strat == strat + 1:
                    p_strat.set_score(current_score+1)
            
            elif p_strat == number_of_strats:
                if strat == 1:
                    p_strat.set_score(current_score-1)
                elif strat == p_strat - 1:
                    p_strat.set_score(current_score-1)
                    
            elif p_strat == 1:
                if strat == p_strat + 1:
                        p_strat.set_score(current_score-1)
                elif strat == number_of_strats:
                    p_strat.set_score(current_score+1)
            
            else:
                if p_strat == strat - 1:
                    p_strat.set_score(current_score-1)
                elif p_strat == strat + 1:
                    p_strat.set_score(current_score+1)
                    
        return current_score
                
                