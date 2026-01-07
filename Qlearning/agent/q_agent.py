import numpy as np
import random

class QAgent:
    def __init__(self, actions=4):
        self.q_table = {}
        self.lr = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.actions = actions

    def get_q(self, state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(self.actions)
        return self.q_table[state]

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.actions - 1)
        return np.argmax(self.get_q(state))

    def learn(self, state, action, reward, next_state):
        q_val = self.get_q(state)[action]
        q_next = max(self.get_q(next_state))
        self.q_table[state][action] = q_val + self.lr * (reward + self.gamma * q_next - q_val)
