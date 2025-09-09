# **Tic-Tac-Toe AI Engine**

## **👋 Intro**

This project is a Python-based Tic-Tac-Toe game that features multiple AI opponents of varying intelligence, culminating in an unbeatable AI using the Minimax algorithm. The goal was to explore fundamental game theory and AI algorithms in a simple, contained environment.

This project was inspired by and follows the excellent tutorials by Robert Heaton on programming projects for advanced beginners:

1. [Building a Tic-Tac-Toe Game Engine](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/)  
2. [Building an Unbeatable Tic-Tac-Toe AI](https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-b/)

## **🛠️ Tech Stack**

* **Python 3:** The entire application is written in Python.  
* **Standard Libraries:** Primarily the copy and itertools libraries for the AI's simulation and tournament setup.

## **✨ Key Features**

* **Human vs. AI & AI vs. AI Gameplay:** Play against any of the developed AI opponents, or pit them against each other.  
* **Multiple AI Opponents:** The engine supports different AI strategies of varying intelligence.  
* **Unbeatable Minimax AI:** A perfect AI that will never lose a game.  
* **Automated Tournament Mode:** A script to run a full tournament between all AIs and generate a detailed performance report.

## **🚀 The Process**

The creation of this project followed an iterative process, starting with the fundamentals and layering on complexity.


**1. The Game Engine**
Following the first Heaton article, the initial step was to build a robust, stateless game engine. This involved creating core functions for creating the board, making moves, and detecting win, lose, or draw conditions.

**2. The Heuristic AIs**
Before tackling the complex Minimax algorithm, several simpler, rule-based (or "heuristic") AIs were developed. The four main AI types are:


1. **Random AI:** Chooses any legally available square at random.

2. **Winning AI:** Scans the board and takes an immediate winning move if available.

3. **Blocking AI:** Adds a defensive layer. It first checks if it can win, then checks if it needs to block an opponent's win.

4. **Unbeatable Minimax AI:** The final and most powerful AI. It uses a recursive search algorithm to find the optimal move, guaranteeing at least a draw.

**3. Implementing Minimax**
The final step was implementing the Minimax algorithm. This AI plays a "perfect" game by assuming the opponent will also play perfectly. Its logic involves a recursive function that explores every possible game outcome and a scoring system (+10 for a win, -10 for a loss, 0 for a draw) to find the path that guarantees the best result.

## **⚙️ Running the Project**

The project is designed to be highly configurable with minimal code changes.

### **Single Game Mode**

To play a single game, open main.py. At the bottom of the file, you will find the if \_\_name\_\_ \== "\_\_main\_\_": block. **You only need to change this one line** to start any matchup you want.

\# In main.py

\# \--- This is the only line you need to change \---  
play(player1\_type="human", player2\_type="minimax")

Simply replace "human" or "minimax" with any of the available player types: "random", "winning", "blocking", or "minimax".

### **🏆 AI Tournament & Analysis**

To get a true measure of each AI's strength, the tournament.py script was created. This script automates the process of testing every AI against every other AI.

How it Works (The run\_tournament function):  
The selected code block orchestrates the entire tournament. Here's a summary of its functionality:

1. **Generates Matchups:** It uses Python's itertools.product to create a list of every possible AI vs. AI pairing from the AI\_PLAYER\_MAP.  
2. **Plays the Games:** For each pairing, it runs a large number of games (e.g., 100\) "silently" in the background for maximum speed.  
3. **Tallies Results:** During the games, it keeps a running count of wins for Player 1 (X), wins for Player 2 (O), and draws.  
4. **Stores Data:** The final win-loss-draw statistics for each matchup are stored in a nested dictionary (all\_results).  
5. **Returns for Display:** Once all matchups are complete, it returns the final results data to be displayed by other functions.

After running, the script displays two clear summaries:

* A **detailed results table** showing the win-loss-draw record for every head-to-head matchup.  
* A **summary bar graph** that ranks each AI by its overall win rate, providing an at-a-glance view of their relative power.

How to Run the Tournament:  
Execute the tournament.py script from your terminal. You can adjust the number of games per matchup by changing the variable at the bottom of the file.  
python tournament.py

## **🎓 Lessons Learned**

* **The Power of State Management:** The most significant challenge was managing the board state during the AI's simulation. The difference between a shallow and a deep copy (copy.deepcopy) is critical.  
* **Consistency is Key:** A subtle but project-breaking bug was caused by an inconsistent coordinate system, teaching a valuable lesson in ensuring data structures are handled consistently across all functions.  
* **Iterative Development:** Building the simple AIs first was invaluable. It allowed for thorough testing of the game engine and provided a clear benchmark against which to measure the Minimax AI's superior logic.

## **💡 Areas for Improvement**

* **Alpha-Beta Pruning:** The current Minimax algorithm could be optimized with alpha-beta pruning to make it more efficient.  
* **GUI:** The game could be enhanced with a graphical user interface using a library like Pygame or Tkinter.