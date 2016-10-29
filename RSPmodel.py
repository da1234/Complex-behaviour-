import math 
import random as rndm

  
class model(object):
    
    def __init__(self, no_strats):
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
        
       # print N_coords
        for n_coord, n_vals in enumerate(N_coords):
           for i,j in enumerate(n_vals):
               
               if j <=grd_sz and j >=1:
                    
                    pass 
                
               else: 
                   # print j
                    j = abs(j-grd_sz)
                    N_coords[n_coord][i] = j
                    #print "this is afterwards",j 
               
        
        #print N_coords           
        return N_coords 
    
    def get_n_values(self, n_coords, grid):
        
        N_values = []
        
        for cords in n_coords:
           # print cords
            N_values.append(grid[cords[0]-1][cords[1]-1])
        
        return N_values  
        
        
        
        
        
    #  this is for the original   
    #def play(self,player,neighbours):
    #    
    #    n_strats = []
    #    p_strat = player.get_strat()
    #    
    #    
    #    
    #    for neighbour in neighbours:
    #        
    #        n_strats.append(neighbour.get_strat())
    #        
    #    #print n_strats
    #    
    #    for n_strat in n_strats:
    #        
    #        current_score = player.get_score()
    #        
    #        if p_strat == 1 and n_strat == 2:
    #            
    #            player.set_score(current_score -1)
    #        
    #        elif p_strat == 1 and n_strat == 3:
    #            
    #             player.set_score(current_score +1)
    #        
    #        elif p_strat == 2 and n_strat == 1:
    #            
    #             player.set_score(current_score +1)
    #             
    #        elif p_strat == 2 and n_strat == 3:
    #            
    #             player.set_score(current_score -1)
    #             
    #        elif p_strat == 3 and n_strat == 1:
    #            
    #             player.set_score(current_score -1)
    #             
    #        elif p_strat == 3 and n_strat == 2:
    #            
    #             player.set_score(current_score +1)
    #             
    #        else: 
    #            pass 
                 
           # print player.get_score()
           
      
        
    def play(self,player,neighbours):
        
            n_strats = []
            player.set_old_strat(player.get_new_strat())
            p_strat = player.get_old_strat()
    
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_old_strat())
            
            for n_strat in n_strats:
                
                current_score = player.get_score()
                
                if p_strat == 1 and n_strat == 2:            
     
                    player.set_score(current_score -1)
            
                elif p_strat == 2 and n_strat == 3:
                
                    player.set_score(current_score -1)
            
                elif p_strat == 3 and n_strat == 1:
                
                    player.set_score(current_score -1)
                    
                else: 
                    pass 
                    
                
                    
                 
    # this is for the original             
    #def change_strat(self, player,neighbours):
    #    
    #    cnt = 0
    #    
    #    n_strats = []
    #    p_score = player.get_score()
    #    
    #    for neighbour in neighbours:
    #        
    #        n_strats.append(neighbour.get_strat())
    #    
    #    
    #
    #    
    #    if p_score <= 0:
    #        
    #        n_av = int(math.ceil(sum(n_strats)/ len(n_strats)))
    #        print n_av
    #        
    #        player.set_strat(n_av)
    #        player.set_score(0)
            
            
                 
    def change_strat(self, player,neighbours):
        
        
        n_strats = []
        p_score = player.get_score()
        
        for neighbour in neighbours:
            
            if neighbour.isColoured() == True:
                  
                n_strats.append(neighbour.get_old_strat())
                
        
        if p_score < 0:
            
            
            if player.get_old_strat() == 1:
                
                player.set_new_strat(2)
                
            
            elif player.get_old_strat() == 2:
                
                player.set_new_strat(3)
            
            elif player.get_old_strat() == 3:
                
                player.set_new_strat(1)
            
            else:
                
                pass 
        
        elif player.get_old_strat() == 0 and len(n_strats)>0:
        
            
            player.set_new_strat(int(math.ceil(sum(n_strats)/ len(n_strats))))
            
            
                            
        
        player.set_score(0)
            
            
        
        
        

                
                
    
    
            
        
            
        
        
        
        
        
        
        
        
        
        
          
        
    
                    
                    
                    
        
        
        
        
        
                
                
                
                 
                    
                
        
        
        
              