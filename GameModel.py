import math 
import random as rndm
import numpy as np 
from matplotlib import pyplot as plt
  
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
            
            if neighbour.is_coloured_double() == True:
                  
                n_strats_black.append(neighbour.get_old_strat())
                
        for neighbour in neighbours:
                     
            n_strats.append(neighbour.get_old_strat())
         
        if p_score < 0:
            
            player.set_new_strat(n_strats[nemesis_indx])
           
        
        elif player.get_old_strat() == [0,0] and len(n_strats_black)>0:
            
            #print "these are the n of the blacks",n_strats 
         
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
                
                current_score = player.get_old_score()
                
                if p_strat == 1:            
                    if n_strat == 2:
                        player.set_old_score(current_score -1)
                    elif n_strat == 3:
                        player.set_old_score(current_score + 1)
            
                elif p_strat == 2:
                    if n_strat == 3:
                        player.set_old_score(current_score -1)
                    elif n_strat == 1:
                        player.set_old_score(current_score + 1)
            
                elif p_strat == 3:
                    if n_strat == 1:
                        player.set_old_score(current_score -1)
                    elif n_strat == 2:
                        player.set_old_score(current_score + 1)
                    
                else: 
                       pass 
                    
    
    #SINGLE STRATS
    def change_strat_single(self, player,neighbours):
        
        n_strats = []
        p_score = player.get_old_score()
        
        for neighbour in neighbours:
            
            if neighbour.is_coloured_single() == True:
                  
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
        
        player.set_old_score(0)
        
    def play_single_2(self,player,neighbours):
        
            n_strats = []
            player.set_old_strat(player.get_new_strat())
            p_strat = player.get_old_strat()
            
            player.set_new_score(0)
    
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_old_strat())
            
            for n_strat in n_strats:
                
                current_score = player.get_new_score()
                
                if p_strat == 1:            
                    if n_strat == 2:
                        player.set_new_score(current_score -1)
                    elif n_strat == 3:
                        player.set_new_score(current_score + 1)
            
                elif p_strat == 2:
                    if n_strat == 3:
                        player.set_new_score(current_score -1)
                    elif n_strat == 1:
                        player.set_new_score(current_score + 1)
            
                elif p_strat == 3:
                    if n_strat == 1:
                        player.set_new_score(current_score -1)
                    elif n_strat == 2:
                        player.set_new_score(current_score + 1)
                    
                else: 
                       pass 
                       
            player.set_old_score(player.get_new_score())
    
    
    def change_strat_single_2(self, player,neighbours):
        
        n_strats = []
        n_scores = []
        p_score = player.get_old_score()
        
        for neighbour in neighbours:
            
            if neighbour.is_coloured_single() == True:
                  
                n_strats.append(neighbour.get_old_strat())
                n_scores.append(neighbour.get_old_score())
         
        if len(n_scores) > 0 and p_score < max(n_scores):
           
            best_n = n_scores.index(max(n_scores))
            best_n_strat = n_strats[best_n]
            
            player.set_new_strat(best_n_strat)
        
        elif player.get_old_strat() == 0 and len(n_strats)>0:
         
            #player.set_new_strat(int(math.ceil(sum(n_strats)/ len(n_strats))))
            player.set_new_strat(n_strats[0])
            
        else:
            pass
        
        #player.set_score(0)
        
        
    #INCLUDES LIZARD, SPOCK FOR SINGLE STRATS
    def play_lizspoc(self,player,neighbours):
        
            n_strats = []
            player.set_old_strat(player.get_new_strat())
            p_strat = player.get_old_strat()
            occurrences = np.zeros(5, dtype=int)
    
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_old_strat())
            
            for n_strat in n_strats:
                
                current_score = player.get_old_score()
                
                if p_strat == 1:            
                    if n_strat == 2 or n_strat == 5: 
                        player.set_old_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 3 or n_strat == 4:
                        player.set_old_score(current_score + 1)
            
                elif p_strat == 2:
                    if n_strat == 3 or n_strat == 4:
                        player.set_old_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 1 or n_strat == 5:
                        player.set_old_score(current_score + 1)
            
                elif p_strat == 3:
                    if n_strat == 1 or n_strat == 5:
                        player.set_old_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 2 or n_strat == 4:
                        player.set_old_score(current_score + 1)
                        
                elif p_strat == 4:
                    if n_strat == 1 or n_strat == 3:
                        player.set_old_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 2 or n_strat == 5:
                        player.set_old_score(current_score + 1)
                        
                elif p_strat == 5:
                    if n_strat == 2 or n_strat == 4:
                        player.set_old_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 1 or n_strat == 3:
                        player.set_old_score(current_score + 1)
                    
                else: 
                       pass 
                       
            return occurrences
                       
                       
    def change_strat_lizspoc(self, player,neighbours, occurrences):
        
        n_strats = []
        p_score = player.get_old_score()
        nemesis = np.argmax(occurrences) + 1
        
        for neighbour in neighbours:
            
            if neighbour.is_coloured_single() == True:
                  
                n_strats.append(neighbour.get_old_strat())
         
        if p_score < 0:
           
            player.set_new_strat(nemesis)
        
        elif player.get_old_strat() == 0 and len(n_strats)>0:
         
            #player.set_new_strat(int(math.ceil(sum(n_strats)/ len(n_strats))))
            player.set_new_strat(n_strats[0])
        
        else:
            pass
        
        player.set_old_score(0)
        
    def play_lizspoc_2(self,player,neighbours):
        
            n_strats = []
            player.set_old_strat(player.get_new_strat())
            p_strat = player.get_old_strat()
            occurrences = np.zeros(5, dtype=int)
    
            player.set_new_score(0)        
            
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_old_strat())
            
            for n_strat in n_strats:
                
                current_score = player.get_new_score()
                
                if p_strat == 1:            
                    if n_strat == 2 or n_strat == 5: 
                        player.set_new_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 3 or n_strat == 4:
                        player.set_new_score(current_score + 1)
            
                elif p_strat == 2:
                    if n_strat == 3 or n_strat == 4:
                        player.set_new_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 1 or n_strat == 5:
                        player.set_new_score(current_score + 1)
            
                elif p_strat == 3:
                    if n_strat == 1 or n_strat == 5:
                        player.set_new_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 2 or n_strat == 4:
                        player.set_new_score(current_score + 1)
                        
                elif p_strat == 4:
                    if n_strat == 1 or n_strat == 3:
                        player.set_new_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 2 or n_strat == 5:
                        player.set_new_score(current_score + 1)
                        
                elif p_strat == 5:
                    if n_strat == 2 or n_strat == 4:
                        player.set_new_score(current_score -1)
                        occurrences[n_strat-1] +=1
                    elif n_strat == 1 or n_strat == 3:
                        player.set_new_score(current_score + 1)
                    
                else: 
                       pass 
                       
            player.set_old_score(player.get_new_score())
                       
            return occurrences
            
    def change_strat_lizspoc_2(self, player,neighbours, occurrences):
        
        n_strats = []
        n_scores = []
        p_score = player.get_old_score()
        nemesis = np.argmax(occurrences) + 1
        
        for neighbour in neighbours:
            
            if neighbour.is_coloured_single() == True:
                  
                n_strats.append(neighbour.get_old_strat())
                n_scores.append(neighbour.get_old_score())
                
        if len(n_scores) > 0 and p_score < max(n_scores):
           
            best_n = n_scores.index(max(n_scores))
            best_n_strat = n_strats[best_n]
            
            player.set_new_strat(best_n_strat)
        
        elif player.get_old_strat() == 0 and len(n_strats)>0:
         
            #player.set_new_strat(int(math.ceil(sum(n_strats)/ len(n_strats))))
            player.set_new_strat(n_strats[0])
        
        else:
            pass
        
        #player.set_score(0)
        
    
    def stability_check(self, all_colours):
        
        stable = False
        indexes = []
            
        first_colour = all_colours[0]
        
        last_value = first_colour[-1]
        first_value = first_colour[0]
        occurrences = first_colour.count(last_value)
        
        if last_value == 0:
            for i in range(1, len(all_colours)):
                colour = all_colours[i]
                final = colour[-1]
                if final != 0:
                    last_value = final
                    first_value = colour[0]
                    occurrences = colour.count(final)
                    first_colour = colour
                    break
                else:
                    pass
                    
        if len(first_colour) == 30:
            count = 0
            for i in first_colour:
                if i == first_value:
                    count += 1
            
            if count == len(first_colour):
                stable = True
            else:
                stable = False
        
        elif occurrences >= 4 and last_value !=0:
            print "Last value:", last_value
            for i in range(len(first_colour)-1, -1, -1):
                if len(indexes) >= 4:
                    break
                elif first_colour[i] == last_value:
                    print "i:", i
                    indexes.append(i)
                else:
                    pass
            print "Indexes:", indexes
            for j in range(len(all_colours)):
                values = []
                for index in indexes:
                    values.append(all_colours[j][index])
                print "Values:", values    
                if values[0] == values[1] and values[0] == values[2] and values[0] == values[3]:
                    stable = True
                else:
                    stable = False
                    break
        else:
            pass
            
        if stable:
            cycle = indexes[0] - indexes[1]
            time = indexes[3]
        else:
            cycle = 0
            time = 0
        
        return stable, time, cycle
            
            
    def euler(self, tMin, tMax, cycle, h, rock, paper, scissors):
        """Calculates the solution using the Explicit Euler method, and plots against time"""
        
        t = np.arange(tMin, tMax, h) 
        r = np.zeros(t.size)
        p = np.zeros(t.size)
        s = np.zeros(t.size)
        r[0] = rock[0]
        p[0] = paper[0]
        s[0] = scissors[0]
        
        points = int(t.size/float(len(rock)))

        a1 = 0.000275
        a2 = 0.000275
        b1 = 0.000275
        b2 = 0.000275
        c1 = 0.000275
        c2 = 0.000275
        
        #rock_max_index = rock.index(max(rock))
        #rock_min_index = rock.index(min(rock))
        #paper_max_index = paper.index(max(paper))
        #paper_min_index = paper.index(min(paper))
        #scissors_max_index = scissors.index(max(scissors))
        #scissors_min_index = scissors.index(min(scissors))
        #
        #a1 = np.log(rock[rock_min_index + 1] / float(rock[rock_min_index]))
        ##a2 = -np.log(rock[rock_max_index + 1] / float(rock[rock_max_index]))
        #b1 = np.log(paper[paper_min_index + 1] / float(paper[paper_min_index]))
        ##b2 = -np.log(paper[paper_max_index + 1] / float(paper[paper_max_index]))
        #c1 = np.log(scissors[scissors_min_index + 1] / float(scissors[scissors_min_index]))
        ##c2 = -np.log(scissors[scissors_max_index + 1] / float(scissors[scissors_max_index]))
        #
        #a2 = a1
        #b2 = b1
        #c2 = c1
        #
        ##total = a1 + a2 + b1 + b2 + c1 + c2
        ##
        #a1 = a1/100.
        #a2 = a2/100.
        #b1 = b1/100.
        #b2 = b2/100.
        #c1 = c1/100.
        #c2 = c2/100.
        
        
        #total = alpha + beta + delta
        
        #if total > 1:
        #    alpha = alpha / float(total)
        #    beta = beta / float(total)   
        #    delta = delta / float(total)
        
        for i in range(1, t.size): #Iteratively obtaining theta values using Explicit Euler
            r[i] = r[i-1] * (1 + h * (a1 * s[i-1] - a2 * p[i-1]))
            p[i] = p[i-1] * (1 + h * (b1 * r[i-1] - b2 * s[i-1]))
            s[i] = s[i-1] * (1 + h * (c1 * p[i-1] - c2 * r[i-1]))
            
        #for i in range(1, len(rock)):
        #    value = i * points
        #    print value
        #    r[int(value)] = rock[i]
        #    print r[int(i*points*h)], rock[i]
        #    p[int(value)] = paper[i]
        #    s[int(value)] = scissors[i]
            
        #print "r:", r
        #print "p:", p
        #print "s:", s
        
        print "a1, a2:", a1, a2
        print "b1, b2:", b1, b2
        print "c1, c2:", c1, c2
        
        #for i in range(1, tMax):
        #    r[i] = rock[0] * np.exp(i * (alpha*scissors[i-1] - beta*paper[i-1]))
        
        plt.figure()
        plt.plot(t, r, 'r', label = "Rock")
        plt.plot(t, p, 'g', label = "Paper")
        plt.plot(t, s, 'b', label = "Scissors")
        plt.title("TEST of PP Model")
        plt.xlabel('Time')
        plt.ylabel('Population')
        plt.legend()
        plt.grid()
        plt.show()
        
        #return r, p, s
                    
        
                                                                                                                                              