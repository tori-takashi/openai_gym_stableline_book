import gym

env = gym.make('CartPole-v1', render_mode="human")

env.reset()
while True:
    env.render()
    env.step(env.action_space.sample())
