#!/usr/bin/env python

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import yaml

# from crazyflie_py import *
# # from crazyflie_py.uav_trajectory import Trajectory
# import yaml

'''
want to see the trajectory cause it is now not that round enough
save the xyz format and use uav gen to visualise it 
'''
def main():
    # load yaml file contains smooth waypoint
    yaml_path = Path(__file__).parent / "data/result_ompl.yaml"
    with open(yaml_path, 'r') as ymlfile:
        data = yaml.safe_load(ymlfile)['result']  # a list  elements are dictionaries
    print('load finish')
    
    
    # height = 0.5
    n = len(data) # number of distinct trajectories
    traj1 = data[0]
    states = traj1['states']  # list len 73
    # print(np.array(states))  # list 
    traj2 = data[1]
    states2 = traj2['states']  # list len 73
    print('states2',states2)


    number = 70
    # Extract x and y coordinates from the points
    x_coords1 = [point[0] for point in states[:number]]
    y_coords1 = [point[1] for point in states[:number]]
    x_coords2 = [point[0] for point in states2[:number]]
    y_coords2 = [point[1] for point in states2[:number]]
    # Plot the points
    # Plot the first set of points in blue
    plt.scatter(x_coords1, y_coords1, color='blue', label='States 1')
    # Plot the second set of points in red
    plt.scatter(x_coords2, y_coords2, color='red', label='States 2')  # [0.762263, 1.01913]
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot of Points')
    plt.grid(True)
    plt.show()

    # print('end')

if __name__ == "__main__":
    main()
