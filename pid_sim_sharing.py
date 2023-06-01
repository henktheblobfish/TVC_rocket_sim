'''
DISCLAIMER: the code is only a template for a simulation, the physics may not be completely accurate, make sure it is realistic for your vehicle.
'''


import math
from math import *
import time
import matplotlib.pyplot as plt

import random
#thrust data from the estes d-12. you will have to replace this with your engine's thrustcurve data. (this function was lazily written by chatGPT, but it works.
def get_thrust(time):
    thrust_data = [
        (0.049, 2.569),
        (0.116, 9.369),
        (0.184, 17.275),
        (0.237, 24.258),
        (0.282, 29.73),
        (0.297, 27.01),
        (0.311, 22.589),
        (0.322, 17.99),
        (0.348, 14.126),
        (0.386, 12.099),
        (0.442, 10.808),
        (0.546, 9.876),
        (0.718, 9.306),
        (0.879, 9.105),
        (1.066, 8.901),
        (1.257, 8.698),
        (1.436, 8.31),
        (1.59, 8.294),
        (1.612, 4.613),
        (1.65, 0.1)
    ]
    
    for i in range(len(thrust_data)):
        if time <= thrust_data[i][0]:
            if i == 0:
                return thrust_data[i][1]
            else:
                time_diff = thrust_data[i][0] - thrust_data[i-1][0]
                thrust_diff = thrust_data[i][1] - thrust_data[i-1][1]
                thrust_per_sec = thrust_diff / time_diff
                time_ratio = (time - thrust_data[i-1][0]) / time_diff
                return thrust_data[i-1][1] + (time_ratio * thrust_per_sec)
    
    return 0.01

'''
calculating angular accelaration
'''

def getrotacc(angle,thrust):
    # Moment of Inertia, replace this with your's.
    rotinertia = 0.02
    # calculating the torque on the rocket. this line uses the angle of your engine in degrees, the thrust and the distance of the swivel point of the engine from the COM.
    swiveldistance = 0.1 # replace this with your engine's swivel point's distance from the COM in meters
    torque = (round(math.cos(radians(90 + angle)),6) * thrust) * swiveldistance
    # acc in radians/s^2 = torque in Nm / inertia in Kg/m
    radacc = torque / rotinertia
    #convert radians to degrees
    degreesacc = degrees(radacc)
    return degreesacc
'''
variables
'''
tvc_angle = 0
thrust = 0

rotv = 0
angleraw =10
angle = angleraw
initial_error=0
#detime between loops is 0.01s
dt = 0.01
clock = 0
tot_angle = 0

'''
matplotlib setup
'''
x = []
y = []

'''
main loop
'''

while True:
    clock += dt
    thrust = get_thrust(clock)
    
    '''
    add your PID controller and engine angle model here. you can use the variables angle, rotv (rotational velocity), thrust, and clock (the time that has passed since ignition) 
    '''
    
    tvc_angle  =  # put your tvc angle output here.
    
    #print(round(output,1))

    rotv += getrotacc(tvc_angle,thrust) * dt
    # Random spin rate deviation, edit this to fit your profile.
    rotv += random.randint(-100,100) / 30
    angle += rotv * dt
    

    print(round(angle,2))
        
    time.sleep(dt)
    # D-12 burns out after 1.65 seconds, change this for your engine.
    if clock > 1.65:
        break
    x.append(clock)
    y.append(angle)

plt.plot(x,y)
plt.show()
