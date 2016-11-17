import math 
import random as rndm
import numpy as np 
  
class model(object):
    
    def __init__(self, no_strats):
           self.no_strats = no_strats
           
        
        
    def get_player_periodic_n(self,p_coords, grd_sz):
        
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
                   #print j
                    j = abs(j-grd_sz)
                    N_coords[n_coord][i] = j
                    #print "this is afterwards",j 
               
         
        #print N_coords         
        return N_coords 
        
    
    def get_player_n(self,p_coords, grd_sz):
        
        N_coords = []
        remove = []
        
        N_coords.append([p_coords[0]+1,p_coords[1]])
        N_coords.append([p_coords[0]-1,p_coords[1]])
        N_coords.append([p_coords[0]-1,p_coords[1]-1])
        N_coords.append([p_coords[0],p_coords[1]+1])
        N_coords.append([p_coords[0],p_coords[1]-1])
        N_coords.append([p_coords[0]-1,p_coords[1]+1])
        N_coords.append([p_coords[0]+1,p_coords[1]-1])
        N_coords.append([p_coords[0]+1,p_coords[1]+1])
             
        for n_coord, n_vals in enumerate(N_coords):
           for i,j in enumerate(n_vals):
               
               if j <=grd_sz and j >=1:
                    pass 
                      
               else: 
                    remove.append(n_vals) 
                    #print n_vals 
                    
        for i in remove:
            if i in N_coords:
                #print i 
                N_coords.remove(i)
                                                               
        return N_coords 
    
     
    def get_n_values(self, n_coords, grid):
        
        N_values = []
        
        for cords in n_coords:
           # print cords
            N_values.append(grid[cords[0]-1][cords[1]-1])
        
        return N_values  
        
           
    def get_ready(self,player):
        
        player.set_old_strat(player.get_new_strat())
        
        
    #DOUBLE STRATS      
    def play_double(self,player,neighbours):
        
            n_strats = []
            #player.set_old_strat(player.get_new_strat())
            p_strat = player.get_old_strat()
            
            results = np.zeros(len(neighbours))
    
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_old_strat())
            
            for indx, n_strat in enumerate(n_strats):
                
                #current_score = player.get_score()   
                
                for k in range(2):
                
                    if p_strat[k] == 1 and n_strat[k] == 2:
               
                       # player.set_score(current_score -1)
                        results[indx] -= 1
            
                    elif p_strat[k] == 1 and n_strat[k] == 3:
                
                        #player.set_score(current_score +1)
                        results[indx] += 1
                
                    elif p_strat[k] == 2 and n_strat[k] == 1:
                
                       # player.set_score(current_score +1)
                        results[indx] += 1
                 
                    elif p_strat[k] == 2 and n_strat[k] == 3:
                
                        #player.set_score(current_score -1)
                        results[indx]-= 1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 1:
                
                       # player.set_score(current_score -1)
                        results[indx] -= 1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 2:
                
                        #player.set_score(current_score +1)
                        results[indx] += 1
                 
                    else: 
                        pass    
            player.set_score(np.sum(results))
            return results
            
    #DOUBLE STRATS
    def change_strat_double(self, player,neighbours,results):
        
        n_strats = []
        n_strats_black = []
        p_score = player.get_score()
        nemesis_indx = np.argmin(results)
        
        for neighbour in neighbours:
            
            if neighbour.isColoured() == True:
                  
                n_strats_black.append(neighbour.get_old_strat())
                
        for neighbour in neighbours:
                     
            n_strats.append(neighbour.get_old_strat())
         
        if p_score < 0:
            
            player.set_new_strat(n_strats[nemesis_indx])
           
        
        elif player.get_old_strat() == [0,0] and len(n_strats_black)>0:
            
            print "these are the n of the blacks",n_strats 
         
            player.set_new_strat(n_strats_black[0])
        
        player.set_score(0)
        
    
    #SINGLE STRATS    
    def play_single(self,player,neighbours):
        
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
                    
    
    #SINGLE STRATS
    def change_strat_single(self, player,neighbours):
        
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
         
            #player.set_new_strat(int(math.ceil(sum(n_strats)/ len(n_strats))))
            player.set_new_strat(n_strats[0])
        
        player.set_score(0)
        
        
    def stability_check(self, all_colours):
    
        peaks_of_colours = []
        peaks_of_colours_indexes = []
        stable = False
        
        for i in range(len(all_colours)):
            
            colour = all_colours[i]
            
            peaks_of_colours.append([])
            peaks_of_colours_indexes.append([])
            
            peaks = peaks_of_colours[i]
            indexes = peaks_of_colours_indexes[i]
            
            for j in range(1, len(colour)-1):
                value = colour[j]
                    
                if value > colour[j-1] and value > colour[j+1]:
                    
                    if i == 0:
                        peaks.append(value)
                        indexes.append(j)
                        stable = False
                    else:
                        if value in peaks and peaks.count(value) >= 3:
                            stable = True
                            break
                        else:
                            peaks.append(value)
                            indexes.append(j)
                            stable = False
                    
        return stable 
        
                 
                          
                                   
                                            
                                                     
                                                              
                                                                       
                                                                                
                                                                                         
                                                                                                  
                                                                                                           
                                                                                                                             