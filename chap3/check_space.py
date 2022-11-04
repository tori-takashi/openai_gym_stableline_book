import gym
import sys
from gym.spaces import *

ENV_ID = sys.argv[1]

def print_spaces(label, space):
    print(label, space)

    if isinstance(space, Box):
        print('最小値：', space.low)
        print('最大値：', space.high)
    
    if isinstance(space, Discrete):
        print('最小値：', 0)
        print('最大値：', space.n-1)

env = gym.make(ENV_ID)

print('環境ID：', ENV_ID)
print_spaces('行動空間：', env.action_space)
print_spaces('状態空間：', env.observation_space)
