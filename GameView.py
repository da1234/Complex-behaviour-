from mesa import Agent, Model
from mesa.time import SimultaneousActivation
import random 
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt
from mesa.batchrunner import BatchRunner
import numpy as np
import math 



##batch_run takeover?

def takeOver(model):

    taken_over = 1

    if model.stable:

        model.running = False

    first_strat = model.schedule.agents[0].get_current_strat()

    for agent,x,y in model.grid.coord_iter():

        if agent.get_current_strat() != first_strat:
            taken_over = 0

    return taken_over 

    



##for the single strats - counting number of strats 
def count_strat1(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==1:

            cnt+=1

    model.R.append(cnt)

    return cnt

def count_strat2(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==2:

            cnt+=1
    model.P.append(cnt)

    return cnt

def count_strat3(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==3:

            cnt+=1

    model.S.append(cnt)

    return cnt

##for the double strats
def count_strat11(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[1,1]:

            cnt+=1
    model.RR.append(cnt)

    return cnt

def count_strat12(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[1,2]:

            cnt+=1
    model.RP.append(cnt)

    return cnt

def count_strat13(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[1,3]:

            cnt+=1
            
    model.RS.append(cnt)

    return cnt
def count_strat21(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[2,1]:

            cnt+=1
    model.PR.append(cnt)

    return cnt

def count_strat22(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[2,2]:

            cnt+=1
    model.PP.append(cnt)
    return cnt

def count_strat23(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[2,3]:

            cnt+=1
    model.PS.append(cnt)
    return cnt

def count_strat31(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[3,1]:

            cnt+=1
            
    model.SR.append(cnt)
    return cnt

def count_strat32(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[3,2]:

            cnt+=1
    model.SP.append(cnt)
    return cnt

def count_strat33(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==[3,3]:

            cnt+=1
    model.SS.append(cnt)
    return cnt

###checking for stability

def stability_check(model):
        
    stable = False
    indexes = []
        
    first_strat = model.all_strats[0]
    
    last_value = first_strat[-1]
    first_value = first_strat[0]
    occurrences = first_strat.count(last_value)
    
    if last_value == 0:
        for i in range(1, len(model.all_strats)):
            strat = model.all_strats[i]
            final = strat[-1]
            if final != 0:
                last_value = final
                first_value = strat[0]
                occurrences = strat.count(final)
                first_strat = strat
                break
            else:
                pass
                
    if len(first_strat) == 30:
        count = 0
        for i in first_strat:
            if i == first_value:
                count += 1
        
        if count == len(first_strat):
            stable = True
        else:
            stable = False
    
    elif occurrences >= 4 and last_value !=0:
        #print("Last value:", last_value)
        for i in range(len(first_strat)-1, -1, -1):
            if len(indexes) >= 4:
                break
            elif first_strat[i] == last_value:
                #print( "i:", i)
                indexes.append(i)
            else:
                pass
        #print("Indexes:", indexes)
        for j in range(len(model.all_strats)):
            values = []
            for index in indexes:
                values.append(model.all_strats[j][index])
            #print("Values:", values)   
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

        
        
    



class GameModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height,SINGLE=False):
        self.num_agents = N
        self.grid = SingleGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)   

        ##for batch runs
        self.running = True
        self.stable = False

        ###keeping track of the numbers of each strat 


        if SINGLE:
            self.R = []
            self.P = []
            self.S = []
            self.all_strats = [self.R,self.P,self.S]

        else:
            self.RR = []
            self.RP = []
            self.RS = []

            self.PR = []
            self.PP = []
            self.PS = []

            self.SR = []
            self.SP = []
            self.SS = []


            
            self.all_strats = [self.RR,self.RP,self.RS,self.PR,self.PP,self.PS,self.SR,self.SP,self.SS]
            
        
        # Create agents
        for i in range(self.num_agents):

            ##R is 1, P is 2, S is 3 btw

            if SINGLE == True:
                strat = random.randint(1,3)
                a = GameAgent(i, self,strat,SINGLE)
                self.schedule.add(a)

                self.datacollector = DataCollector(model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3,
                                                                    "takeOver":takeOver})
            else:
                strat1= random.randint(1,3)
                strat2 = random.randint(1,3)

                #print(strat1,strat2)
                a = GameAgent(i, self,[strat1,strat2],SINGLE)
                self.schedule.add(a)                
                self.datacollector = DataCollector(model_reporters ={"strat11 cnt":count_strat11,"strat12 cnt":count_strat12,"strat13 cnt":count_strat13,
                             "strat21 cnt":count_strat21,"strat22 cnt":count_strat22,"strat23 cnt":count_strat23,
                             "strat31 cnt":count_strat31,"strat32 cnt":count_strat32,"strat33 cnt":count_strat33,
                                                                 "takeOver":takeOver})               


                
            # Add the agent to a random grid cell

            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)

            while not self.grid.is_cell_empty((x,y)):
                x = random.randrange(self.grid.width)
                y = random.randrange(self.grid.height)

            self.grid.place_agent(a, (x, y))

##        self.datacollector = DataCollector(
##            model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3})
##
                

    def step(self):
        self.datacollector.collect(self)
        self.stabilised()
        self.schedule.step()

    def stabilised(self):

        stability_state,time,cycle = stability_check(self)
        self.stable = stability_state

    



class GameAgent(Agent):
    
    """ An RPS player """
    def __init__(self, unique_id, model,strategy,single):
        super().__init__(unique_id, model)

        self.score= 0
        self.id = unique_id
        self.single = single
        self.current_strategy = strategy
        self.next_strategy = strategy

    def set_next_strat(self, n_strat):
       
        self.next_strategy = n_strat
      
    def get_next_strat(self):
        
        return self.next_strategy 
        
    def set_current_strat(self, n_strat):
       
        self.current_strategy = n_strat
      
    def get_current_strat(self):
        
        return self.current_strategy 
        
    def get_score(self):
        return self.score
        
    def set_score(self, n_score):
        
        self.score = n_score

        

    def play(self):

        if self.single:

            self._play_single()
        else:
            self._play_double()
            

        
    

    def _play_single(self):

        n_strats = []
 
        p_strat = self.get_current_strat()

        neighbours = self.model.grid.get_neighbors(
            self.pos,
            moore=True,
            include_center=False, radius=1)

        self.results = np.zeros(len(neighbours))
    
        for neighbour in neighbours:
                
            n_strats.append(neighbour.get_current_strat())
        #print("these are the neighbour strats",n_strats)
            
        for indx, n_strat in enumerate(n_strats):

 #           current_score = self.get_score()

            if p_strat == 1 and n_strat == 2:
               
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                        
            
            elif p_strat == 1 and n_strat == 3:
                
 #                   self.set_score(current_score +1)
                    self.results[indx] += 1
                    
                
            elif p_strat == 2 and n_strat == 1:
                
 #                   self.set_score(current_score +1)
                    self.results[indx] += 1
     
                 
            elif p_strat== 2 and n_strat == 3:
                
#                    self.set_score(current_score -1)
                    self.results[indx] -= 1
 
                 
            elif p_strat == 3 and n_strat == 1:
                
#                    self.set_score(current_score -1)
                    self.results[indx] -= 1
 
                 
            elif p_strat == 3 and n_strat == 2:
                
#                    self.set_score(current_score +1)
                    self.results[indx] += 1
                
            else:
                    pass
        self.set_score(np.sum(self.results))

        #print("this is the players score and id",self.unique_id, self.get_score())


    def _play_double(self):
        
            n_strats = []
            #player.set_old_strat(player.get_new_strat())
            p_strat = self.get_current_strat()

            #print("p strat",p_strat)

            
            neighbours = self.model.grid.get_neighbors(
             self.pos,
             moore=True,
             include_center=False, radius=1)

            self.results = np.zeros(len(neighbours))
    
    
            for neighbour in neighbours:
                
                n_strats.append(neighbour.get_current_strat())
            
            for indx, n_strat in enumerate(n_strats):
                
                #current_score = player.get_score()   
                
                for k in range(2):
                
                    if p_strat[k] == 1 and n_strat[k] == 2:
               
                       # player.set_score(current_score -1)
                        self.results[indx] -= 1
            
                    elif p_strat[k] == 1 and n_strat[k] == 3:
                
                        #player.set_score(current_score +1)
                        self.results[indx] += 1
                
                    elif p_strat[k] == 2 and n_strat[k] == 1:
                
                       # player.set_score(current_score +1)
                        self.results[indx] += 1
                 
                    elif p_strat[k] == 2 and n_strat[k] == 3:
                
                        #player.set_score(current_score -1)
                        self.results[indx]-= 1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 1:
                
                       # player.set_score(current_score -1)
                        self.results[indx] -= 1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 2:
                
                        #player.set_score(current_score +1)
                        self.results[indx] += 1
                 
                    else: 
                        pass    
            self.set_score(np.sum(self.results))
            #return results
 
 

    def update_strat(self):
        
         n_strats = []
         p_score = self.get_score()
         nemesis_indx = np.argmin(self.results)

         neighbours = self.model.grid.get_neighbors(
            self.pos,
            moore=True,
            include_center=False, radius=1)
        
         for neighbour in neighbours:

            n_strats.append(neighbour.get_current_strat())

         if p_score < 0:
            
            self.set_next_strat(n_strats[nemesis_indx])
 
         else:
                pass
    
            
         self.set_score(0)



        

    def get_ready(self):
        
        self.set_current_strat(self.get_next_strat())
    
    def step(self):
        self.play()
        self.update_strat()
    

    def advance(self):
        self.get_ready()
        


##x = GameModel(100,10,10,False)
##
##while (x.running):
##    x.step()
##
####for i in range(300):
####    x.step()
##    #print(x.schedule.agents[i].get_score())
##graph = x.datacollector.get_model_vars_dataframe()
##graph.plot()
##plt.xlabel("Clock Ticks")
##plt.ylabel("Number of Players")
##plt.legend(loc=2)
##plt.grid()    
##plt.show()
##plt.show()


def takeOver_prob(run_data):
    prob = 0
    total = 0
    no_runs = len(run_data.takeOver)
    
    for i in run_data.takeOver:
        
        total+= i
	
    prob = total/no_runs

    print(prob)
    return prob 
    

    

##parameters = {"width": 10,
##             "height": 10,
##              "N": 100,
##              "SINGLE":False}
##
##batch_run = BatchRunner(GameModel,
##                        parameters,
##                        iterations=100,
##                        max_steps=300,
##                        model_reporters={"takeOver":takeOver})
##batch_run.run_all()
##
##
##run_data = batch_run.get_model_vars_dataframe()
####run_data.head()
##
##takeOver_prob(run_data)


# 0.42, 0.46, 0.45 for 8x8 agents
##0.26, 0.19, 0.15, 0.23, 0.24
##plt.scatter(run_data.N, run_data.Gini)


def get_hist_data(Single,width,height,N):

    probs_array = np.zeros(100)

    for i in range(20):
    

        parameters = {"width": width,
                 "height": height,
                  "N": N,
                  "SINGLE":Single}

        batch_run = BatchRunner(GameModel,
                            parameters,
                            iterations=100,
                            max_steps=300,
                            model_reporters={"takeOver":takeOver})
        batch_run.run_all()


        run_data = batch_run.get_model_vars_dataframe()


        prob = takeOver_prob(run_data)

        probs_array[i] = prob

    return probs_array


#hist_data = get_hist_data(False,5,5,25)
#print(hist_data)


for size in range(1,10):
##
    hist_data = get_hist_data(False,size,size,size**2)
    np.savetxt('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizeData/' + str(size)+'.txt',hist_data)
##

    

    










        
