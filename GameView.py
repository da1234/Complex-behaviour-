from mesa import Agent, Model
from mesa.time import SimultaneousActivation
import random 
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt
from mesa.batchrunner import BatchRunner
import numpy as np
import math 


###mutations

def mutate_single(model):
    percent = 0.5
    number_of_mutations = int(model.num_agents * percent)

    players_to_mutate = []
    player_ids = []
    # all_players = model.schedule.agents[random.randint(0, 6399)]
    i = 0

    if model.stable and model.mutate_count < 1:
        model.mutate_count += 1
        while i < number_of_mutations:

            random_player = model.schedule.agents[random.randint(0, 6399)]

            if random_player.id not in player_ids:
                player_ids.append(random_player.id)
                players_to_mutate.append(random_player)
                i += 1

        for player in players_to_mutate:

            current_strat = player.current_strategy

            if current_strat == 1:
                player.next_strategy = random.randint(2, 3)
            elif current_strat == 2:
                player.next_strategy = random.randrange(1, 4, 2)
            elif current_strat == 3:
                player.next_strategy = random.randint(1, 2)

    print(len(players_to_mutate))

    




###Frustration 
def Frustration2(model):
        
    cnt =0

    if model.beg ==False:

        for player,x,y in model.grid.coord_iter():

            n_strats = []
            p_strat = player.get_current_strat()

            for neighbs in model.grid.get_neighbors(
            player.pos,
            moore=True,
            include_center=False, radius=1):   
                
                n_strats.append(neighbs.get_current_strat())
            
            for indx, n_strat in enumerate(n_strats):
                  
                
                for k in range(2):
                
                    if p_strat[k] == 1 and n_strat[k] == 2:
               
                       cnt+=1
                        
            
                    elif p_strat[k] == 1 and n_strat[k] == 3:
                
                        pass
                
                    elif p_strat[k] == 2 and n_strat[k] == 1:
                
                        pass
                 
                    elif p_strat[k] == 2 and n_strat[k] == 3:

                        cnt+=1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 1:
                
                       cnt+=1
                 
                    elif p_strat[k] == 3 and n_strat[k] == 2:
            
                       pass
                 
                    else: 
                        pass

    model.beg=False

    return cnt
    
            

def Frustration(model):

    cnt =0

    if model.beg ==False:

        for player,x,y in model.grid.coord_iter():

            for neighbs in model.grid.get_neighbors(
            player.pos,
            moore=True,
            include_center=False, radius=1):

                if player.get_current_strat() !=neighbs.get_current_strat():
            
                    cnt+=1
                    
    model.beg=False

    return cnt



###counting the number of score 

def count_draw(model):

    cnt =0

    if model.beg ==False:

        for player,x,y in model.grid.coord_iter():

            if player.get_prev_score() <0:

                    cnt+=1
    model.beg=False

    return cnt



###determining the spread of similar strats

def var11(model):

    if model.beginning[11] == True:

        var = 0

        model.beginning[11] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[1,1]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.RR_var = var

    return model.RR_var

def var12(model):

    if model.beginning[12] == True:

        var = 0

        model.beginning[12] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[1,2]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.RP_var=var

    return model.RP_var
           
def var13(model):

    if model.beginning[13] ==True:

        var = 0

        model.beginning[13] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[1,3]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.RS_var=var

    return model.RS_var

def var21(model):

    if model.beginning[21] == True:

        var = 0

        model.beginning[21] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[2,1]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.PR_var=var

    return model.PR_var

def var22(model):

    if model.beginning[22] == True:

        var = 0

        model.beginning[22] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[2,2]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.PP_var=var

    return model.PP_var

def var23(model):

    if model.beginning[23] == True:

        var = 0

        model.beginning[23] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[2,3]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.PS_var=var

    return model.PS_var

def var31(model):

    if model.beginning[31] == True:

        var = 0

        model.beginning[31] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[3,1]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.SR_var=var

    return model.SR_var

def var32(model):

    if model.beginning[32] == True:

        var = 0

        model.beginning[32] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[3,2]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.SP_var=var

    return model.SP_var

def var33(model):

    if model.beginning[33] == True:

        var = 0

        model.beginning[33] = False

        pos = []

        for player,x,y in model.grid.coord_iter():

            if player.get_current_strat() ==[3,3]:

                pos.append([x,y])


        pos = np.asarray(pos)

        std = np.std(pos)
        var = std
        model.SS_var=var      

    return model.SS_var



##whats in the batch_run equilibrium

def Equilibrium(model):

    if model.stable:

        model.running = False


        for agent,x,y in model.grid.coord_iter():

            first_strat = agent.get_current_strat()[0]
            second_strat = agent.get_current_strat()[1]

            model.equilib[str(first_strat)+str(second_strat)]=1

    return model.equilib 






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

def count_strat4(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==4:

            cnt+=1

    model.L.append(cnt)
    return cnt


def count_strat5(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==5:

            cnt+=1

    model.SP.append(cnt)
    
    return cnt

def count_strat6(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==6:

            cnt+=1

    model.A.append(cnt)
    return cnt


def count_strat7(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==7:

            cnt+=1

    model.F.append(cnt)
    return cnt


def count_strat8(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==8:

            cnt+=1

    model.G.append(cnt)
    return cnt


def count_strat9(model):
    cnt = 0

    for player,x,y in model.grid.coord_iter():

        if player.get_current_strat() ==9:

            cnt+=1

    model.H.append(cnt)
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
    def __init__(self, N, width, height,SINGLE=False, LIZSPOC=False,NINEWAY=False):
        self.num_agents = N
        self.grid = SingleGrid(width, height, True)
        self.schedule = SimultaneousActivation(self)   

        ##for batch runs
        self.running = True
        self.stable = False
        ##collecting initial data
        self.beg=True
        self.beginning = {11:True,12:True,13:True,21:True,22:True,23:True,31:True,32:True,33:True}
        self.equilib = {}
        

        ###keeping track of the numbers of each strat 


        if SINGLE:
            self.R = []
            self.P = []
            self.S = []
            self.all_strats = [self.R,self.P,self.S]

        elif LIZSPOC:

            self.R = []
            self.P = []
            self.S = []
            self.L = []
            self.SP = []
            self.all_strats = [self.R,self.P,self.S, self.L, self.SP]

        elif NINEWAY:

            self.R = []
            self.P = []
            self.S = []
            self.SP = []
            self.L = []
            self.A = []
            self.F = []
            self.G = []
            self.H = []
            self.all_strats = [self.R,self.P,self.S, self.SP, self.L, self.A, self.F, self.G, self.H]


  
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


            self.RR_var=0
            self.RP_var=0
            self.RS_var=0

            self.PR_var=0
            self.PP_var=0
            self.PS_var=0

            self.SR_var=0
            self.SP_var=0
            self.SS_var=0


            
            self.all_strats = [self.RR,self.RP,self.RS,self.PR,self.PP,self.PS,self.SR,self.SP,self.SS]
            
        
        # Create agents
        for i in range(self.num_agents):

            ##R is 1, P is 2, S is 3 btw

            if SINGLE == True:
                strat = random.randint(1,3)
                a = GameAgent(i, self,strat,SINGLE,LIZSPOC,NINEWAY)
                self.schedule.add(a)

                self.datacollector = DataCollector(model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3,
                                                                        "takeOver":takeOver})

            elif LIZSPOC == True:
                strat = random.randint(1,5)
                a = GameAgent(i, self,strat,SINGLE,LIZSPOC,NINEWAY)
                self.schedule.add(a)

                self.datacollector = DataCollector(model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3, "strat4 cnt":count_strat4, "strat5 cnt":count_strat5,
                                                                    "takeOver":takeOver})


            elif NINEWAY == True:
                strat = random.randint(1,9)
                a = GameAgent(i, self,strat,SINGLE,LIZSPOC,NINEWAY)
                self.schedule.add(a)

##                self.datacollector = DataCollector(model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3, "strat4 cnt":count_strat4, "strat5 cnt":count_strat5, "strat6 cnt":count_strat6, "strat7 cnt":count_strat7, "strat8 cnt":count_strat8, "strat9 cnt":count_strat9,
##                                                                    "takeOver":takeOver})
                self.datacollector = DataCollector(model_reporters={"strat1 cnt":count_strat1,"strat2 cnt":count_strat2,"strat3 cnt":count_strat3, "strat4 cnt":count_strat4, "strat5 cnt":count_strat5, "strat6 cnt":count_strat6, "strat7 cnt":count_strat7, "strat8 cnt":count_strat8, "strat9 cnt":count_strat9,"score 0":count_draw,})
##            

##            
            else:
                strat1= random.randint(1,3)
                strat2 = random.randint(1,3)

                #print(strat1,strat2)
                a = GameAgent(i, self,[strat1,strat2],SINGLE,LIZSPOC,NINEWAY)
                self.schedule.add(a)                
##                self.datacollector = DataCollector(model_reporters ={"strat11 cnt":count_strat11,"strat12 cnt":count_strat12,"strat13 cnt":count_strat13,
##                             "strat21 cnt":count_strat21,"strat22 cnt":count_strat22,"strat23 cnt":count_strat23,
##                             "strat31 cnt":count_strat31,"strat32 cnt":count_strat32,"strat33 cnt":count_strat33,
##                                                                     "var11":var11,"var12":var12,"var13":var13,
##                                                                     "var21":var21,"var22":var22,"var23":var23,
##                                                                     "var31":var31,"var32":var32,"var33":var33,
##                                                                     "Equilibrium":Equilibrium
##                                                                 })
                
                self.datacollector = DataCollector(model_reporters ={"strat11 cnt":count_strat11,"strat12 cnt":count_strat12,"strat13 cnt":count_strat13,
                             "strat21 cnt":count_strat21,"strat22 cnt":count_strat22,"strat23 cnt":count_strat23,
                             "strat31 cnt":count_strat31,"strat32 cnt":count_strat32,"strat33 cnt":count_strat33,"score 0":count_draw,"Frust":Frustration,
                                            
                                                                     "Equilibrium":Equilibrium
                                                                 }) 


                
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
    def __init__(self, unique_id, model,strategy,single,lizspoc,nineway):
        super().__init__(unique_id, model)

        self.score= 0
        self.prev_score=0
        self.id = unique_id
        self.single = single
        self.lizspoc = lizspoc
        self.nineway = nineway
        self.current_strategy = strategy
        self.next_strategy = strategy
        self.mutate_count = 0


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

    def get_prev_score(self):
        return self.prev_score
        
    def set_prev_score(self, n_score):
        
        self.prev_score = n_score
        

    def play(self):

        if self.single:

            self._play_single()

        elif self.lizspoc:
            self._play_lizspoc()

        elif self.nineway:
            self._play_nineway()

            
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
        

            
    def _play_lizspoc(self):

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

            if p_strat == 1:
                if n_strat == 2 or n_strat == 5:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 3 or n_strat == 4:
                    self.results[indx] += 1

            elif p_strat == 2:
                if n_strat == 3 or n_strat == 4:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat == 5:
                    self.results[indx] += 1

            elif p_strat == 3:
                if n_strat == 1 or n_strat == 5:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 4:
                    self.results[indx] += 1

            elif p_strat == 4:
                if n_strat == 1 or n_strat == 3:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 5:
                    self.results[indx] += 1

            elif p_strat == 5:
                if n_strat == 2 or n_strat == 4:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat == 3:
                    self.results[indx] += 1

            else:
                    pass
        self.set_score(np.sum(self.results))

        #print("this is the players score and id",self.unique_id, self.get_score())

    def _play_nineway(self):

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

            if p_strat == 1:
                if n_strat == 2 or n_strat == 5 or n_strat == 6 or n_strat == 8:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 3 or n_strat == 4 or n_strat == 7 or n_strat == 9:
                    self.results[indx] += 1

            elif p_strat == 2:
                if n_strat == 3 or n_strat == 4 or n_strat == 7 or n_strat == 9:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat == 5 or n_strat == 6 or n_strat == 8:
                    self.results[indx] += 1

            elif p_strat == 3:
                if n_strat == 1 or n_strat == 5 or n_strat == 7 or n_strat == 8:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 4 or n_strat == 6 or n_strat == 9:
                    self.results[indx] += 1

            elif p_strat == 4:
                if n_strat == 1 or n_strat == 3 or n_strat == 7 or n_strat == 9:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 5 or n_strat == 6 or n_strat == 8:
                    self.results[indx] += 1

            elif p_strat == 5:
                if n_strat == 2 or n_strat == 4 or n_strat == 6 or n_strat == 9:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat == 3 or n_strat == 7 or n_strat == 8:
                    self.results[indx] += 1

            elif p_strat == 6:
                if n_strat == 2 or n_strat == 3 or n_strat == 4 or n_strat == 9:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat ==5 or n_strat == 7 or n_strat == 8:
                    self.results[indx] += 1

            elif p_strat == 7:
                if n_strat == 1 or n_strat == 5 or n_strat == 6 or n_strat == 8:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 3 or n_strat == 4 or n_strat == 9:
                    self.results[indx] += 1

            elif p_strat == 8:
                if n_strat == 2 or n_strat == 4 or n_strat == 5 or n_strat == 6:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 1 or n_strat == 3 or n_strat == 7 or n_strat == 9:
                    self.results[indx] += 1

            elif p_strat == 9:
                if n_strat == 1 or n_strat == 3 or n_strat == 7 or n_strat == 8:
 #                   self.set_score(current_score -1)
                    self.results[indx] -= 1
                elif n_strat == 2 or n_strat == 4 or n_strat == 5 or n_strat == 6:
                    self.results[indx] += 1

            else:
                    pass
        self.set_score(np.sum(self.results))



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
    

##         self.set_prev_score(p_score)           
##         self.set_score(0)



    def get_ready(self):

        ###trying to record scores 
        self.set_prev_score(self.get_score())           
        self.set_score(0)
        self.set_current_strat(self.get_next_strat())
    
    def step(self):
        self.play()
        self.update_strat()
    

    def advance(self):
        self.get_ready()
        


##x = GameModel(100,10,10,SINGLE=False,LIZSPOC=False,NINEWAY=False)
##
##while (x.running):
########    #print(x.all_strats)
##   x.step()
##
##g= x.datacollector.get_model_vars_dataframe()
##print(g.head(400))
######
######for i in range(300):
######    x.step()
####    #print(x.schedule.agents[i].get_score())
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
    

    
def get_hist_data(width,height,N,Single,Lizspoc,nineway):

    probs_array = np.zeros(20)

    for i in range(20):
    

        parameters = {"width": width,
                 "height": height,
                  "N": N,
                  "SINGLE":Single,
                      "LIZSPOC":Lizspoc,
                      "NINEWAY":nineway,
                      }
        

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



def get_spread_data(Single,Lizspoc,width,height,N):



        parameters = {"width": width,
                 "height": height,
                  "N": N,
                  "SINGLE":Single,
                      "LIZSPOC":Lizspoc}
        

        batch_run = BatchRunner(GameModel,
                            parameters,
                            iterations=100,
                            max_steps=300,
                            model_reporters={"var11":var11,"var12":var12,"var13":var13,
                                                                     "var21":var21,"var22":var22,"var23":var23,
                                                                     "var31":var31,"var32":var32,"var33":var33,
                                             "Equilibrium":Equilibrium})

        batch_run.run_all()


        run_data = batch_run.get_model_vars_dataframe()

        print(run_data.head(99))


#get_spread_data(Single=False,Lizspoc=False,width=8,height=8,N=64)


    


#hist_data = get_hist_data(Single=False,Lizspoc=False,nineway=True,width,height,N
#print(hist_data)


##for size in range(17,19,2):
##    hist_data = get_hist_data(size,size,size**2,Single=False,Lizspoc=False,nineway=True)
##    np.savetxt('/Users/darrelladjei/python/bsc/mesaStuff/SystemSizeData/nineway' + str(size)+'.txt',hist_data)





##
##x = GameModel(100,10,10,SINGLE=True,LIZSPOC=False,NINEWAY=False)
####
##while (x.running):
##########    #print(x.all_strats)
##   x.step()
####
##g= x.datacollector.get_model_vars_dataframe()
##print(g.head(400))
########
##for i in range(300):
##    x.step()
##    #print(x.schedule.agents[i].get_score())
##graph = x.datacollector.get_model_vars_dataframe()
##graph.plot()
##plt.xlabel("Clock Ticks")
##plt.ylabel("Number of Players")
##plt.legend(loc=2)
##plt.grid()    
##plt.show()
##plt.show()
    

        










        
