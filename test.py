from agentenv_babyai.environment import BabyAIEnv

env = BabyAIEnv()
# Creat 100 environments
for i in range(100):
    # This just create an environment, but not reset it
    env.create()

i = 0 # index of the environment
j = 0 # index of the game type, from 0 to 39
data = env.reset(i, j)
print(env.render(i))
# print(f"data: {data}")
# print(f"obs: {data['observation']}")
print(f"goal: {env.env[i]._get_goal()}")
print(env.step(i, "go to grey key 4"))
print(env.render(i))
print(env.step(i, "pickup grey key 1"))
print(env.render(i))
print(env.step(i, "move forward"))
print(env.render(i))
# print(env.step(i, "turn right"))
# print(env.render(i))
# print(env.reset(0, 0))
# print(env.render(0))