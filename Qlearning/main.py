import pygame
from game.snake_game import SnakeGame
from agent.q_agent import QAgent
from pygame.time import Clock

pygame.init()

game = SnakeGame()
agent = QAgent()

episodes = 500

clock = Clock()

for episode in range(episodes):
    state = game.reset()
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        action = agent.choose_action(state)
        next_state, reward, done = game.step(action)
        
        agent.learn(state, action, reward, next_state)
        state = next_state
        
        game.render()
        clock.tick(8)

    agent.epsilon *= agent.epsilon_decay
    print("Episode:", episode, "Score:", game.score)

pygame.quit()
