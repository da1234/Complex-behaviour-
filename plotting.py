#LINES 164 - 169
no_of_greens = []
no_of_blues = []
no_of_reds = []

counter = 0
clock_ticks = []

#LINES 189 - 190
counter += 1
clock_ticks.append(counter)
    
    
#LINES 209 - 211
green = 0
blue = 0
red = 0

green += 1 #LINE 218
blue += 1 #LINE 222
red += 1 #LINE 226

#LINES 236 - 238
no_of_greens.append(green)
no_of_blues.append(blue)
no_of_reds.append(red)

#LINES 246 - 257
print "Clock Ticks:", clock_ticks
print "List of Greens:", no_of_greens
print "List of Blues:", no_of_blues
print "List of Reds:", no_of_reds

plt.plot(clock_ticks, no_of_greens, 'g')
plt.plot(clock_ticks, no_of_blues, 'b')
plt.plot(clock_ticks, no_of_reds, 'r')
plt.xlabel("Clock Ticks")
plt.ylabel("Number of Players")
plt.grid()
plt.show()
