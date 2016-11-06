"""
 potential framework for RPS grid 
"""
import pygame
import numpy as np 
import random as rndm
import player as pl 
import RSPmodel as m
import matplotlib.pyplot as plt
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

MAROON =(128,0,0)
CRIMSON = (220,20,60)

NAVY = (0,0,128)
ROYAL_BLUE = (65,105,225)

LIGHT_GREEN = (144,238,144)
DARK_GREEN = (0,100,0)


##pausing stuff 
pause =False 

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 5
HEIGHT = 5
 
# This sets the margin between each cell
MARGIN = 5

##for plotting 
no_of_greens = []
no_of_blues = []
no_of_reds = []
no_of_light_greens = []
no_of_dark_greens = []
no_of_maroons = []
no_of_crimsons= []
no_of_navys = []
no_of_royals = []




counter = 0
clock_ticks = []

#initialising the model 
model = m.model(3)
 
# initialising Board 
grid = []
grd_sz = 80
      
for row in range(grd_sz+1):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(grd_sz+1):
        
        player = pl.Player([0,0])
        grid[row].append(player)
        


#trying to random distribution
#for i in range(100):
#        
#    x=rndm.randint(1,79)
#    y=rndm.randint(1,79)
#    r1 = rndm.randint(1,3)
#    r2 = rndm.randint(1,3)
#    
#    print "these are the deviants",x,y,r1,r2
#        
#    grid[x][y].set_old_strat([r1,r2])
#    grid[x][y].set_new_strat([r1,r2])

        
        
        
 #trying to segment the page    
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
    
    
    
    ##for plotting 
    counter += 1
    
    #if counter == 210:
    #    
    #    done = True 
    
    clock_ticks.append(counter)
    
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
            n_coords = model.get_player_8_n(plyr_coords,grd_sz) #model.get_player_n(plyr_coords,grd_sz)
            n_values = model.get_n_values(n_coords, grid)
            results = model.play(grid[row_pos][col_pos],n_values)
            model.change_strat(grid[row_pos][col_pos],n_values, results)
                          
 
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    
    
    
    ##for plotting 
    green = 0
    blue = 0
    red = 0
    maroon =0
    crimson =0
    navy = 0
    royal_blue = 0
    light_green =0
    dark_green=0
    
    
    for row in range(grd_sz):
        for column in range(grd_sz):
            color = BLACK

            
            if grid[row][column].get_old_strat() == [1,1]:
                color = GREEN
                green+=1
                
            elif grid[row][column].get_old_strat() == [2,2]:
                color = BLUE
                blue+=1
                
            elif grid[row][column].get_old_strat() == [3,3]:
                color = RED
                red+=1
                
            elif grid[row][column].get_old_strat() == [1,2]:
                color = LIGHT_GREEN
                light_green+=1
                
            elif grid[row][column].get_old_strat() == [1,3]:
                color = DARK_GREEN
                dark_green+=1
                
            elif grid[row][column].get_old_strat() == [2,1]:
                color = NAVY
                navy+=1
                
            elif grid[row][column].get_old_strat() == [2,3]:
                color = ROYAL_BLUE
                royal_blue+=1
                
            elif grid[row][column].get_old_strat() == [3,1]:
                color = MAROON
                maroon+=1
                
            elif grid[row][column].get_old_strat() == [3,2]:
                color = CRIMSON
                crimson+=1
              
            pygame.draw.rect(screen,color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
      
    no_of_greens.append(green)
    no_of_blues.append(blue)
    no_of_reds.append(red)
    no_of_light_greens.append(light_green)
    no_of_dark_greens.append(dark_green)
    no_of_maroons.append(maroon)
    no_of_crimsons.append(crimson)
    no_of_navys.append(navy)
    no_of_royals.append(royal_blue)
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.


print "Clock Ticks:", clock_ticks
print "List of Greens:", no_of_greens
print "List of Blues:", no_of_blues
print "List of Reds:", no_of_reds
print "List of light_greens:", no_of_light_greens
print "List of dark_greens:", no_of_dark_greens
print "List of crimsons:", no_of_crimsons
print "List of maroons:", no_of_maroons
print "List of navy blue:", no_of_navys
print "List of royal blues:", no_of_royals


plt.plot(clock_ticks, no_of_greens, 'g--')
plt.plot(clock_ticks, no_of_blues, 'b--')
plt.plot(clock_ticks, no_of_reds, 'r--')
plt.plot(clock_ticks, no_of_light_greens,'g-')
plt.plot(clock_ticks, no_of_dark_greens, 'go')
plt.plot(clock_ticks, no_of_maroons, 'r-')
plt.plot(clock_ticks, no_of_crimsons, 'ro')
plt.plot(clock_ticks, no_of_navys, 'b-')
plt.plot(clock_ticks, no_of_royals, 'bo')
plt.xlabel("Clock Ticks")
plt.ylabel("Number of Players")
plt.grid()
plt.show()

pygame.quit()