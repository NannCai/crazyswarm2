#!/usr/bin/env python

import numpy as np
from pathlib import Path

from crazyflie_py import *
# from crazyflie_py.uav_trajectory import Trajectory
import yaml

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
    
    
    height = 0.5
    n = len(data) # number of distinct trajectories
    traj1 = data[0]
    states = traj1['states']  # lisrt len 73
    print(states)  # list 
    print('end')




if __name__ == "__main__":
    main()
