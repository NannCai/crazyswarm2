#!/usr/bin/env python

import numpy as np
from pathlib import Path

from crazyflie_py import *
# from crazyflie_py.uav_trajectory import Trajectory
import yaml

'''
the first states is the position
the last is the x y way point
'''
def main():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs  # CrazyflieServer

    allcfs.takeoff(targetHeight=0.5, duration=2.0)
    timeHelper.sleep(2)

    # load yaml file contains smooth waypoint
    yaml_path = Path(__file__).parent / "data/result_ompl.yaml"
    with open(yaml_path, 'r') as ymlfile:
        data = yaml.safe_load(ymlfile)['result']  # a list  elements are dictionaries
    print('load finish')
    
    
    height = 0.5
    n = len(data) # number of distinct trajectories
    traj1 = data[0]
    states = traj1['states']  # list len 73
    # print(type(states))  # list 
    for cf in allcfs.crazyflies:
        pos = np.append(np.array(states[0]), height)
        print('pos',pos)
        cf.goTo(pos, 0, 2.0)  # goal yaw duration
    for state in states[1:]:  # state list
        print('state:',state)
        pos = np.append(np.array(state), height)
        for cf in allcfs.crazyflies:
            cf.goTo(pos, 0, 5.0)  # goal yaw duration
        # timeHelper.sleep(2)
        print('1')

    # timeHelper.sleep(2)
    # allcfs.land(targetHeight=0.06, duration=2.0)


if __name__ == "__main__":
    main()
