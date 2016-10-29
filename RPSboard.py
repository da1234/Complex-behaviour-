"""
 potential framework for RPS grid 
"""
import pygame
import numpy as np 
import random as rndm
import player as pl 
import RSPmodel as m
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 5
HEIGHT = 5
 
# This sets the margin between each cell
MARGIN = 5

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
        player = pl.Player(0)
        grid[row].append(player)
        
        
## trying to segment the page    
for i in range(26):
    for j in range(26):
    
        grid[i][j].set_old_strat(1)
        grid[i][j].set_new_strat(1)

for i in range(26,51,1):
    for j in range(26):
    
        grid[i][j].set_old_strat(2)
        grid[i][j].set_new_strat(2)

for i in range(51,81,1):   
    for j in range(21):
    
        grid[i][j].set_old_strat(3)
        grid[i][j].set_new_strat(3)
 ####       
        
for i in range(26):
    for j in range(26,51,1):
    
        grid[i][j].set_old_strat(3)
        grid[i][j].set_new_strat(3)

for i in range(26,51,1):
    for j in range(26,51,1):
    
        grid[i][j].set_old_strat(1)
        grid[i][j].set_new_strat(1)

for i in range(51,81,1):   
    for j in range(25,51,1):
    
        grid[i][j].set_old_strat(2)
        grid[i][j].set_new_strat(2)
##

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
    
        grid[i][j].set_old_strat(1)
        grid[i][j].set_new_strat(1)
        


##starting with 1 pixel of two 
#for row in range(grd_sz+1):
#    # Add an empty array that will hold each cell
#    # in this row
#    grid.append([])
#    for column in range(grd_sz+1):
#        player = pl.Player(1)
#        grid[row].append(player)
#
#
#grid[40][20].set_old_strat(3)
#grid[40][20].set_new_strat(3)
#
#grid[40][60].set_old_strat(2)
#grid[40][60].set_new_strat(2)

    
    
## this gave random results      
#for i in range(6):
#    
#    strat = rndm.randint(1,3) 
#    
#    grid[rndm.randint(1,159)][rndm.randint(1,159)].set_old_strat(strat)
#    grid[rndm.randint(1,159)][rndm.randint(1,159)].set_new_strat(strat)
    
      

 
        
#this was the original 
#        
#for row in range(grd_sz):
#    # Add an empty array that will hold each cell
#    # in this row
#    
#    grid.append([])
#    
#    for column in range(grd_sz):
#        #grid[row].append(0)  # Append a cell
#        player = pl.Player(rndm.randint(1,3))
#        grid[row].append(player)
 

 
   
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
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        
            
    #else
        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #     # User clicks the mouse. Get the position
        #    pos = pygame.mouse.get_pos()
        #    # Change the x/y screen coordinates to grid coordinates
        #    column = pos[0] // (WIDTH + MARGIN)
        #    row = pos[1] // (HEIGHT + MARGIN)
        #    # Set that location to one
        #    grid[row][column].set_new_strat(1) 
            
            
            
            
    #for each player get his neighbours coords and play  
            
    for row_pos,row_values in enumerate(grid):
        for col_pos,col_val in enumerate(row_values):
                        
                    #print row_pos+1,col_pos+1
                        
            plyr_coords = [row_pos+1,col_pos+1]
            n_coords = model.get_player_n(plyr_coords,grd_sz)
            n_values = model.get_n_values(n_coords, grid)
            model.play(grid[row_pos][col_pos],n_values)
            model.change_strat(grid[row_pos][col_pos],n_values)
                          
 
    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid
    for row in range(grd_sz):
        for column in range(grd_sz):
            color = BLACK
            if grid[row][column].get_old_strat() == 1:
                color = GREEN
                
            elif grid[row][column].get_old_strat() == 2:
                color = BLUE
                
            elif grid[row][column].get_old_strat() == 3:
                color = RED
                
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()