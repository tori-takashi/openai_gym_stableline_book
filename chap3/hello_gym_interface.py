import gym

env = gym.make('BipedalWalker-v3', render_mode="human")
state = env.reset()

while True:
    env.render()
    action = env.action_space.sample()

    observation, reward, terminated, truncated, info = env.step(action)

    print("################")
    print('observation:', observation)
    print('reward:', reward)
    print('terminated', terminated)
    print('truncated:', truncated)
    print('info', info)
    
    if terminated:
        print('done')
        break

env.close()