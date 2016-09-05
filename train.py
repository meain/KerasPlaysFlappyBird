from model import model
from qlearning4k import Agent
from flappy_bird import FlappyBird

game = FlappyBird(frame_rate=10000, sounds=False)
agent = Agent(model, memory_size=-1)
agent.train(game, epsilon=[0.1, 0.01], epsilon_rate=0.05, gamma=0.99, nb_epoch=10000, batch_size=32, observe=0, checkpoint=250)
