# 🐍 Snake AI using Q-Learning (Reinforcement Learning)

This project implements the **Snake Game** and trains an **AI Agent using Q-Learning** to play and improve automatically.  
The snake starts dumb, learns from its mistakes, avoids danger, finds food intelligently, and keeps improving through experience.

---

## 🚀 What’s New in This Version?
This upgraded version includes:

✔ **Bigger Board (600x600)**  
✔ **Visible Grid** – clear movement visualization  
✔ **Reduced Speed** – easier to observe learning  
✔ **Smarter State Representation with Danger Detection**
- danger straight  
- danger left  
- danger right  
✔ **Food Direction Awareness**  
✔ More stable learning performance  

---

## 🎯 Objective
Train the snake to:
- Survive longer  
- Avoid walls and its own body  
- Efficiently move toward food  
- Learn optimal movement patterns through experience  

This project demonstrates reinforcement learning in a simple, visual, and interactive way.

---

## 🧠 What is Q-Learning?
Q-Learning is a **Reinforcement Learning** algorithm where an agent learns by interacting with the environment.

The AI:
1️⃣ Takes an action  
2️⃣ Receives a reward or penalty  
3️⃣ Updates its knowledge  
4️⃣ Gradually improves behavior  

The knowledge is stored in a **Q-Table**:

```
Q[state][action]
```

Meaning:
“How good is taking this action in this situation?”

---

## 📌 How It Works

### 1️⃣ Game Environment
The game environment handles:
- Snake movement  
- Food spawning  
- Collision detection  
- Reward assignment  
- State generation for the agent  

---

### 2️⃣ State Representation (What AI Sees)

```
(
 danger_straight,
 danger_left,
 danger_right,

 food_left,
 food_right,
 food_up,
 food_down
)
```

This helps snake:
✔ Avoid danger  
✔ Navigate safely  
✔ Move intelligently toward food  

---

### 3️⃣ Actions (What AI Can Do)

```
0 = Left
1 = Right
2 = Up
3 = Down
```

---

### 4️⃣ Rewards System

| Event | Reward |
|------|--------|
| Eats food | +10 |
| Dies | -10 |
| Normal movement | 0 |

This ensures:
- AI prefers survival  
- AI is encouraged to eat food  
- AI learns safe navigation  

---

### 5️⃣ Q-Learning Formula

```
Q(s,a) = Q(s,a) + α * ( reward + γ * max(Q(s’)) − Q(s,a) )
```

Where:
- α (alpha) → Learning Rate  
- γ (gamma) → Discount Factor  
- reward → environment feedback  
- s → current state  
- s’ → next state  

---

### 6️⃣ Exploration vs Exploitation
Uses **Epsilon-Greedy Strategy**:

```
epsilon = 1.0          
epsilon_decay = 0.995  
```

Starts fully random → gradually becomes smarter.

---

## 🏗 Project Structure

```
Snake-QLearning/
│
├── game/
│   ├── __init__.py
│   └── snake_game.py
│
├── agent/
│   ├── __init__.py
│   └── q_agent.py
│
├── main.py
├── requirements.txt
├── README.md
```

---

## 🛠 Installation

### 1️⃣ Go to project folder
```
cd Snake-QLearning
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Project
```
python main.py
```

You will see:
- Snake game window  
- Grid board  
- Snake moving  
- AI gradually improving  
- Training logs printing per episode  

---

## 👀 What You Will Notice
Beginning:
- Random movement  
- Frequent deaths  

After some training:
- Avoids walls  
- Avoids own body  
- Moves intelligently toward food  
- Survives longer  

This is Reinforcement Learning in action 🎯

---

## 🌟 Why This Project is Useful

Helps understand:
- Reinforcement Learning  
- Q-Learning  
- Reward Engineering  
- State Representation  
- AI in Games  

Perfect for:
✔ Students  
✔ AI Beginners  
✔ Projects & Research  
✔ Resume Portfolio  

---

## 🚀 Future Improvements
You can enhance further by:
- Better body awareness  
- Distance-based rewards  
- Deep Q-Learning (Neural Network)  
- Save & Load trained agent  
- Training performance graphs  

---

## 🙌 Credits
Built to learn and demonstrate **AI + Reinforcement Learning** in a fun and visual way.

---
