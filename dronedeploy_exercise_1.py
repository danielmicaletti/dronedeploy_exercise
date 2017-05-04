# Drone Airspace Coding Challenge

# Given a square airspace, 128km x 128km, and N=10,000 drones occupying the airspace
# our challenge is to efficiently compute how many drones are flying too close to one 
# another. 

# Drone positions will be provided as an Nx2 array of [x,y] coordinates (in meters).
# Drones must maintain a horizontal separation of radius 0.5km from other drones. 

# If a drone is within 0.5km of another drone, both are "in conflict".
# Have count_conflicts return the total number of drones that are in a conflicted state. 
# Not the total number of conflicts).

# Do all of your work and testing in this pad. 
# Some common libraries can be imported, but not all, so relying on niche algorithm won't work. 
# This is very solvable with standard python libraries, several ways. 

# Coding style, readability, scalability, and documentation all matter! Consider the 
# computational complexity of your solution. 

# The N^2 answer can be coded up in 5 minutes and # 10 lines; we'd like to see something better!
#from math import sqrt
import numpy
import random
random.seed(1)  # Setting random number generator seed for repeatability

NUM_DRONES = 10000
AIRSPACE_SIZE = 128000  # Meters.
CONFLICT_RADIUS = 500  # Meters.

def count_conflicts(drones, conflict_radius):
    #To be transparent, I found this solution online and implemented it.
    
    drones_in_conflict = 0
    
    # Create list representing airspace with 0's
    airspace = numpy.zeros(shape=(AIRSPACE_SIZE, AIRSPACE_SIZE))
    
    # Add drone positions to list represented by 1's 
    airspace[zip(*drones)] = 1
    
    #Iterate through drones to determine if drone is in conflicting airspace
    for i,d in enumerate(drones):
        conflict_space = airspace[d[0] - conflict_radius : d[0] + conflict_radius, d[1] - conflict_radius : d[1] + conflict_radius]
        if conflict_space.any():
            drones_in_conflict +=1
            
    return drones_in_conflict
        

def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts = count_conflicts(positions, CONFLICT_RADIUS)
print "Drones in conflict: {}".format(conflicts)