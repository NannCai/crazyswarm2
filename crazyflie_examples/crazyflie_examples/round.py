#!/usr/bin/env python

import numpy as np
from pathlib import Path

from crazyflie_py import *
# from crazyflie_py.uav_trajectory import Trajectory
import yaml

height = 0.5
'''
the first states is the position
the last is the x y way point
'''
def one_traj():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs  # CrazyflieServer

    # load yaml file contains smooth waypoint
    yaml_path = Path(__file__).parent / "data/result_ompl.yaml"
    with open(yaml_path, 'r') as ymlfile:
        data = yaml.safe_load(ymlfile)['result']  # a list  elements are dictionaries
    print('load finish')

    traj1 = data[0]
    states = traj1['states']  # list len 73

    allcfs.takeoff(targetHeight=1.0, duration=2.0)
    timeHelper.sleep(2.5)

    #initial position
    pos = np.append(np.array(states[0]), height)
    print('pos',pos)
    for cf in allcfs.crazyflies:
        cf.goTo(pos, 0, 2.0)  # goal yaw duration
    # timeHelper.sleep(2)

    for state in states[1:]:  # state list
        print('state:',state)
        pos = np.append(np.array(state), height)
        for cf in allcfs.crazyflies:
            cf.goTo(pos, 0, 6.0)  # goal yaw duration
        print('1')

    timeHelper.sleep(5)
    allcfs.land(targetHeight=0.06, duration=2.0)

def multi_traj():
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs  # CrazyflieServer

    # load yaml file contains smooth waypoint
    yaml_path = Path(__file__).parent / "data/result_ompl.yaml"
    with open(yaml_path, 'r') as ymlfile:
        data = yaml.safe_load(ymlfile)['result']  # a list  elements are dictionaries
    print('load finish')

    height = 0.5
    n = len(data) # number of distinct trajectories
    states_list = []
    for i in range(n):
        states = data[i]['states']
        states_list.append(states)
    # print('states_list',states_list)

    allcfs.takeoff(targetHeight=0.5, duration=2.0)
    timeHelper.sleep(2)
    print('len(states_list[0])',len(states_list[0]))
    for state_id in range(len(states_list[0])):  # 73  can goto synchronized for multi drones?
        for drone_id in range(len(allcfs.crazyflies)): # 2
            togo_time = 10.0
            if state_id ==1:
                pos = np.append(np.array(states_list[drone_id][state_id]), height)
                allcfs.crazyflies[drone_id].goTo(pos, 0, togo_time)
                timeHelper.sleep(togo_time/2)
            else:

                pos = np.append(np.array(states_list[drone_id][state_id]), height)
                # print(states_list[drone_id])
                print('drone_id',drone_id,'state_id',state_id)
                print(len(allcfs.crazyflies))
                allcfs.crazyflies[drone_id].goTo(pos, 0, togo_time)
            # timeHelper.sleep(1)


    timeHelper.sleep(togo_time + 1)
    allcfs.land(targetHeight=0.06, duration=2.0)


    quit()



    traj1 = data[0]
    states = traj1['states']  # list len 73
    # print(type(states))  # list 
    #initial position
    pos = np.append(np.array(states[0]), height)
    print('pos',pos)
    for cf in allcfs.crazyflies:
        cf.goTo(pos, 0, 2.0)  # goal yaw duration
    timeHelper.sleep(2)

    for state in states[1:]:  # state list
        print('state:',state)
        pos = np.append(np.array(state), height)
        for cf in allcfs.crazyflies:
            cf.goTo(pos, 0, 6.0)  # goal yaw duration
        print('1')

    timeHelper.sleep(5)
    allcfs.land(targetHeight=0.06, duration=2.0)


def main():
    # one_traj()
    multi_traj()

if __name__ == "__main__":
    main()
