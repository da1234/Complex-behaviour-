"""
 potential framework for RPS grid 
"""
import pygame
import numpy as np 
import random as rndm
import PlayerModel as pl 
import GameModel as m
import matplotlib.pyplot as plt
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ORANGE = (255,128,0)
YELLOW =(255, 255,0)
PURPLE = (153,51,255)

PINK = (255,153,255)
BROWN = (102,51,0)
CYAN = (0,255,255)


##pausing stuff 
global pause

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 5
HEIGHT = 5
 
# This sets the margin between each cell
MARGIN = 5

#Changing between single and double strats
SINGLE = True

#Changing between standard RPS and extended LS version for single strats
LIZSPOC = False

#Changing between PRE-DETERMINED or RANDOM Initial Conditions
RANDOM = True

#Changing between PERIODIC and NON-PERIODIC Boundary Conditions
PERIODIC = False


##for plotting 

no_of_reds = []
no_of_greens = []
no_of_blues = []
all_colours = [no_of_reds, no_of_greens, no_of_blues]

if SINGLE and LIZSPOC:
    no_of_purples = []
    no_of_oranges = []
    all_colours.extend((no_of_purples, no_of_oranges))
    
elif not SINGLE:
    no_of_oranges = []
    no_of_yellows = []
    no_of_purples = []
    
    no_of_pinks= []
    no_of_browns = []
    no_of_cyans = []
    
    all_colours.extend((no_of_oranges, no_of_yellows, no_of_purples, no_of_pinks, no_of_browns, no_of_cyans))

counter = 0
clock_ticks = []

#initialising the model 
model = m.model(3)
 
# initialising Board 
grid = []
grd_sz = 80


if SINGLE:
    
    #SINGLE strat
    for row in range(grd_sz+1):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(grd_sz+1):
            
            player = pl.Player(0, SINGLE)
            grid[row].append(player)
            
    
    if LIZSPOC:
        if RANDOM:
        #trying to random distribution SINGLE
            #for i in range(100):
            #        
            #    x=rndm.randint(1,grd_sz)
            #    y=rndm.randint(1,grd_sz)
            #    r1 = rndm.randint(1,5)
            #    
            #    #print "these are the deviants",x,y,r1,r2
            #        
            #    grid[x][y].set_old_strat(r1)
            #    grid[x][y].set_new_strat(r1)
                
            for i in range(grd_sz):
                for j in range(grd_sz):
                    
                    r1 = rndm.randint(1, 5)
                
                    grid[i][j].set_old_strat(r1)
                    grid[i][j].set_new_strat(r1)
        else:
            for i in range(26):
                for j in range(26):
            
                    grid[i][j].set_old_strat(1)
                    grid[i][j].set_new_strat(1)
        
            for i in range(26,51,1):
                for j in range(26):
                
                    grid[i][j].set_old_strat(2)
                    grid[i][j].set_new_strat(2)
            
            for i in range(51,81,1):   
                for j in range(26):
                
                    grid[i][j].set_old_strat(3)
                    grid[i][j].set_new_strat(3)
            ####       
                    
            for i in range(26):
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(4)
                    grid[i][j].set_new_strat(4)
            
            for i in range(26,51,1):
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(5)
                    grid[i][j].set_new_strat(5)
            
            for i in range(51,81,1):   
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(1)
                    grid[i][j].set_new_strat(1)
            ###
            
            for i in range(26):
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(2)
                    grid[i][j].set_new_strat(2)
            
            for i in range(26,51,1):
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(3)
                    grid[i][j].set_new_strat(3)
            
            for i in range(51,81,1):   
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(4)
                    grid[i][j].set_new_strat(4)

    
    else:
        if RANDOM:
        #trying to random distribution SINGLE
            #for i in range(100):
            #        
            #    x=rndm.randint(1,79)
            #    y=rndm.randint(1,79)
            #    r1 = rndm.randint(1,3)
            #    
            #    #print "these are the deviants",x,y,r1,r2
            #        
            #    grid[x][y].set_old_strat(r1)
            #    grid[x][y].set_new_strat(r1)
                
            for i in range(grd_sz):
                for j in range(grd_sz):
                    
                    r1 = rndm.randint(1, 3)
                
                    grid[i][j].set_old_strat(r1)
                    grid[i][j].set_new_strat(r1)
            
        else:   
            #trying to segment the page   SINGLE STRAT  
            for i in range(26):
                for j in range(26):
                
                    grid[i][j].set_old_strat(1)
                    grid[i][j].set_new_strat(1)
            
            for i in range(26,51,1):
                for j in range(26):
                
                    grid[i][j].set_old_strat(2)
                    grid[i][j].set_new_strat(2)
            
            for i in range(51,81,1):   
                for j in range(26):
                
                    grid[i][j].set_old_strat(3)
                    grid[i][j].set_new_strat(3)
            ####       
                    
            for i in range(26):
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(2)
                    grid[i][j].set_new_strat(2)
            
            for i in range(26,51,1):
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(3)
                    grid[i][j].set_new_strat(3)
            
            for i in range(51,81,1):   
                for j in range(26,51,1):
                
                    grid[i][j].set_old_strat(1)
                    grid[i][j].set_new_strat(1)
            ###
            
            for i in range(26):
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(3)
                    grid[i][j].set_new_strat(3)
            
            for i in range(26,51,1):
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(1)
                    grid[i][j].set_new_strat(1)
            
            for i in range(51,81,1):   
                for j in range(51,81,1):
                
                    grid[i][j].set_old_strat(2)
                    grid[i][j].set_new_strat(2)


else:
    #DOUBLE Strat
    for row in range(grd_sz+1):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(grd_sz+1):
            
            player = pl.Player([0,0], SINGLE)
            grid[row].append(player)
            
    
    if RANDOM:
        #trying to random distribution DOUBLE
        for i in range(100):
                
            x=rndm.randint(1,79)
            y=rndm.randint(1,79)
            r1 = rndm.randint(1,3)
            r2 = rndm.randint(1,3)
            
            #print "these are the deviants",x,y,r1,r2
                
            grid[x][y].set_old_strat([r1,r2])
            grid[x][y].set_new_strat([r1,r2])       
            
            
    else:
        #trying to segment the page    DOUBLE STRAT 
        for i in range(26):
            for j in range(26):
            
                grid[i][j].set_old_strat([1,1])
                grid[i][j].set_new_strat([1,1])
        
        for i in range(26,51,1):
            for j in range(26):
            
                grid[i][j].set_old_strat([2,2])
                grid[i][j].set_new_strat([2,2])
        
        for i in range(51,81,1):   
            for j in range(26):
            
                grid[i][j].set_old_strat([3,3])
                grid[i][j].set_new_strat([3,3])
        ####       
                
        for i in range(26):
            for j in range(26,51,1):
            
                grid[i][j].set_old_strat([1,2])
                grid[i][j].set_new_strat([1,2])
        
        for i in range(26,51,1):
            for j in range(26,51,1):
            
                grid[i][j].set_old_strat([1,3])
                grid[i][j].set_new_strat([1,3])
        
        for i in range(51,81,1):   
            for j in range(26,51,1):
            
                grid[i][j].set_old_strat([2,1])
                grid[i][j].set_new_strat([2,1])
        ###
        
        for i in range(26):
            for j in range(51,81,1):
            
                grid[i][j].set_old_strat([2,3])
                grid[i][j].set_new_strat([2,3])
        
        for i in range(26,51,1):
            for j in range(51,81,1):
            
                grid[i][j].set_old_strat([3,1])
                grid[i][j].set_new_strat([3,1])
        
        for i in range(51,81,1):   
            for j in range(51,81,1):
            
                grid[i][j].set_old_strat([3,2])
                grid[i][j].set_new_strat([3,2])
            
   
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800,800]#[255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def unpaused():
    global pause
    pause = False

def paused():
    
    global done 
    
    while pause: 
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                unpaused()
                done = True 
                
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                unpaused()
            

 
# -------- Main Program Loop -----------
while not done:
    global pause
    
    
    
    ###for plotting 
    clock_ticks.append(counter)
    counter += 1
    
    
    #if counter == 200:
    #   
    #    done = True 
    
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
            
    #else
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pause = True 
            paused()
            
        #     # User clicks the mouse. Get the position
        #    pos = pygame.mouse.get_pos()
        #    # Change the x/y screen coordinates to grid coordinates
        #    column = pos[0] // (WIDTH + MARGIN)
        #    row = pos[1] // (HEIGHT + MARGIN)
        #    # Set that location to one
        #    grid[row][column].set_new_strat(1) 
            
            
            
      # each player should get ready for the next game 
      
    for row_pos,row_values in enumerate(grid):
        for col_pos,col_val in enumerate(row_values):
            
            model.get_ready(grid[row_pos][col_pos])
      
            
                        
    #for each player get his neighbours coords and play  
            
    for row_pos,row_values in enumerate(grid):
        for col_pos,col_val in enumerate(row_values):
                        
                    #print row_pos+1,col_pos+1
                        
            plyr_coords = [row_pos+1,col_pos+1]
            
            if PERIODIC:
                n_coords = model.get_player_periodic_n(plyr_coords,grd_sz)
            else:
                n_coords = model.get_player_n(plyr_coords,grd_sz)
                
            n_values = model.get_n_values(n_coords, grid)
            
            
            if SINGLE and LIZSPOC:
                occurrences = model.play_lizspoc(grid[row_pos][col_pos],n_values)
                model.change_strat_lizspoc(grid[row_pos][col_pos],n_values, occurrences)
            elif SINGLE and not LIZSPOC:
                model.play_single(grid[row_pos][col_pos],n_values)
                model.change_strat_single(grid[row_pos][col_pos],n_values)
            else:
                results = model.play_double(grid[row_pos][col_pos],n_values)
                model.change_strat_double(grid[row_pos][col_pos],n_values, results)
                          
 
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    
    ##FOR PLOTTING 
    red = 0
    green = 0
    blue = 0
        
    if SINGLE and LIZSPOC:
        purple = 0
        orange = 0
    
    elif not SINGLE:
        orange = 0
        yellow = 0
        purple = 0
        pink = 0
        brown = 0
        cyan = 0 
        
    if SINGLE:
        
        for row in range(grd_sz):
            for column in range(grd_sz):
                color = BLACK
    
                
                if grid[row][column].get_old_strat() == 1:
                    color = RED
                    red += 1
                    
                elif grid[row][column].get_old_strat() == 2:
                    color = GREEN
                    green += 1
                    
                elif grid[row][column].get_old_strat() == 3:
                    color = BLUE
                    blue += 1
                    
                if LIZSPOC:
                    
                    if grid[row][column].get_old_strat() == 4:
                        color = PURPLE
                        purple += 1
                    
                    elif grid[row][column].get_old_strat() == 5:
                        color = ORANGE
                        orange += 1
                
                pygame.draw.rect(screen,color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
                                
        no_of_reds.append(red)
        no_of_greens.append(green)
        no_of_blues.append(blue)
        
        if LIZSPOC:
            no_of_purples.append(purple)
            no_of_oranges.append(orange)
        
    else:
        
        for row in range(grd_sz):
            for column in range(grd_sz):
                color = BLACK
    
                
                if grid[row][column].get_old_strat() == [1,1]:
                    color = RED
                    red += 1
                    
                elif grid[row][column].get_old_strat() == [1,2]:
                    color = GREEN
                    green += 1
                    
                elif grid[row][column].get_old_strat() == [1,3]:
                    color = BLUE
                    blue += 1
                    
                elif grid[row][column].get_old_strat() == [2,1]:
                    color = ORANGE
                    orange += 1
                    
                elif grid[row][column].get_old_strat() == [2,2]:
                    color = YELLOW
                    yellow += 1
                    
                elif grid[row][column].get_old_strat() == [2,3]:
                    color = PURPLE
                    purple += 1
                    
                elif grid[row][column].get_old_strat() == [3,1]:
                    color = PINK
                    pink += 1
                    
                elif grid[row][column].get_old_strat() == [3,2]:
                    color = BROWN
                    brown += 1
                    
                elif grid[row][column].get_old_strat() == [3,3]:
                    color = CYAN
                    cyan += 1
                
                pygame.draw.rect(screen,color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
      
        no_of_greens.append(green)
        no_of_blues.append(blue)
        no_of_reds.append(red)
        
        no_of_oranges.append(orange)
        no_of_yellows.append(yellow)
        no_of_purples.append(purple)
        
        no_of_pinks.append(pink)
        no_of_browns.append(brown)
        no_of_cyans.append(cyan)
    
    stability, time, cycle = model.stability_check(all_colours)
    
    if stability:
        done=True
        print "Stability reached after ", time, " clock ticks."
        print "Stabilty cycle = ", cycle, " clock ticks."
        
        
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
#print all_colours

max_value = 0
min_value = 100000
for colour in all_colours:
    if max(colour) > max_value:
        max_value = max(colour)
    if min(colour) < min_value:
        min_value = min(colour)
    
stable_time = []
stable_reds = []
stable_greens = []
stable_blues = []
for i in range(time, len(clock_ticks)):
    stable_time.append(i)
    stable_reds.append(no_of_reds[i])
    stable_greens.append(no_of_greens[i])
    stable_blues.append(no_of_blues[i])
    

#print "Clock Ticks:", clock_ticks
#print "List of Reds:", no_of_reds
#print "List of Greens:", no_of_greens
#print "List of Blues:", no_of_blues

#if not SINGLE:
#    print "List of Oranges:", no_of_oranges
#    print "List of Yellows:", no_of_yellows
#    print "List of Purples:", no_of_purples
#    print "List of Pinks:", no_of_pinks
#    print "List of Browns:", no_of_browns
#    print "List of Cyans:", no_of_cyans
    
if SINGLE:    
    plt.plot(stable_time, stable_reds, 'r', label="Strat: 1 (Rock)")
    plt.plot(stable_time, stable_greens, 'g', label="Strat: 2 (Paper)")
    plt.plot(stable_time, stable_blues, 'b', label="Strat: 3 (Scissors)")
    if LIZSPOC:
        plt.plot(clock_ticks, no_of_purples, 'purple', label="Strat: 4 (Lizard)")
        plt.plot(clock_ticks, no_of_oranges, 'orange', label="Strat: 5 (Spock)")
    
    if RANDOM:  
        if PERIODIC:
            plt.title("Population of Each SINGLE Strategy Against Time (RANDOM, PERIODIC)")
        else:
            plt.title("Population of Each SINGLE Strategy Against Time (RANDOM, NON-PERIODIC)")
    else:
        if PERIODIC:
            plt.title("Population of Each SINGLE Strategy Against Time (NON-RANDOM, PERIODIC)")
        else:
            plt.title("Population of Each SINGLE Strategy Against Time (NON-RANDOM, NON-PERIODIC)")
    
else:    
    plt.plot(clock_ticks, no_of_reds, 'r', label="Strat: [1, 1]")
    plt.plot(clock_ticks, no_of_greens, 'g', label="Strat: [1, 2]")
    plt.plot(clock_ticks, no_of_blues, 'b', label="Strat: [1, 3]")
    plt.plot(clock_ticks, no_of_oranges,'orange', label="Strat: [2, 1]")
    plt.plot(clock_ticks, no_of_yellows, 'yellow', label="Strat: [2, 2]")
    plt.plot(clock_ticks, no_of_purples, 'purple', label="Strat: [2, 3]")
    plt.plot(clock_ticks, no_of_pinks, 'pink', label="Strat: [3, 1]")
    plt.plot(clock_ticks, no_of_browns, 'brown', label="Strat: [3, 2]")
    plt.plot(clock_ticks, no_of_cyans, 'cyan', label="Strat: [3, 3]")
    if RANDOM:  
        if PERIODIC:
            plt.title("Population of Each DOUBLE Strategy Against Time (RANDOM, PERIODIC)")
        else:
            plt.title("Population of Each DOUBLE Strategy Against Time (RANDOM, NON-PERIODIC)")
    else:
        if PERIODIC:
            plt.title("Population of Each DOUBLE Strategy Against Time (NON-RANDOM, PERIODIC)")
        else:
            plt.title("Population of Each DOUBLE Strategy Against Time (NON-RANDOM, NON-PERIODIC)")
            
#plt.axvline(time, color='k', linestyle='--')
#plt.annotate('Stability after \n' +str(time) + ' clock ticks',
#            xy=(time, max_value),  # theta, radius
#            xytext=(0.8, 0.75),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='black', shrink=0.0005),
#            horizontalalignment='right',
#            verticalalignment='top',
#            )
#plt.axvline(time+cycle, color='m', linestyle='--')
#plt.annotate('Cycle Period: ' +str(cycle),
#            xy=(time + cycle, min_value + 1),  # theta, radius
#            xytext=(0.8, 0.25),    # fraction, fraction
#            textcoords='figure fraction',
#            arrowprops=dict(facecolor='black', shrink=0.0005),
#            horizontalalignment='right',
#            verticalalignment='top',
#            )
plt.xlabel("Clock Ticks")
plt.ylabel("Number of Players")
plt.legend(loc=2)
plt.grid()
plt.show()

#r, p, s = model.euler(clock_ticks[-1], 0.005, no_of_blues[0], no_of_greens[0], no_of_reds[0])
#plt.plot(clock_ticks, r, '--')
#plt.plot(clock_ticks, p, '--')
#plt.plot(clock_ticks, s, '--')

model.euler(time, clock_ticks[-1], cycle, 0.00005, stable_reds, stable_greens, stable_blues)

#0.00005

#plt.figure()
#plt.hist(no_of_greens)
#plt.title("Histogram of rocks")
#plt.xlabel("No of Rocks")
#plt.ylabel("Occurences")
#plt.grid()
#plt.show()

#red_dif = [0]
#green_dif = [0]
#blue_dif = [0]
#
#for i in range(1, len(no_of_reds)):
#    dif1= no_of_reds[i] - no_of_reds[i-1]
#    red_dif.append(dif1)
#    dif2= no_of_greens[i] - no_of_greens[i-1]
#    green_dif.append(dif2)
#    dif3= no_of_blues[i] - no_of_blues[i-1]
#    blue_dif.append(dif3)

#plt.figure()
#plt.plot(clock_ticks, np.zeros(len(clock_ticks)), 'y')
#plt.plot(clock_ticks, red_dif, 'r--')
#plt.plot(clock_ticks, green_dif, 'g--')
#plt.plot(clock_ticks, blue_dif, 'b--')
#plt.title("Changes in stategy population between consecutive points")
#plt.xlabel("Time")
#plt.ylabel("Difference between consecutive points")
#plt.grid()
#plt.show()

pygame.quit()
