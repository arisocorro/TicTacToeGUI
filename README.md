# Tic-Tac-Toe GUI with MinMax AI

An implementation of MinMax AI algorithm on Tic-Tac-Toe with Tkinter GUI 

![Screenshot 2024-01-30 135740](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/2926a957-94aa-4d75-a02c-648583db8fe9)

##Introduction

For this project I decided to design and develop a GUI for Tic-Tac-Toe. I used tkinter due to its simplicity since my focus for this project was the implementation of the minmax AI algorithm. To solve games using this AI, we first need to map out all potential moves for the AI as well as the human player.  I used a tree data structure, where each level of the tree corresponds with whose turn it is and each node being the state of the board after the play. Alternating between the player and the AI until the game’s conclusion in either a win, a loss or a tie from the perspective of the AI.
 In my version of the game, X doesn’t necessarily have you go first, because I didn’t know that was a rule, and when I asked by friends, they concurred. In that case, the root node will always be the human player. Every time the player places an X or O on the grid, that becomes the new root node from which all further nodes will stem from. We call these nodes the “children” of the root or “parent” node. This is a recursive algorithm, meaning that each of the children with have their own set of children until it reaches the end state of the game where it will return the conclusion: whether the AI wins, loses, or ties. The status of the conclusion in Tic-Tac-Toe is determined by whether one of the players gets a line of three and wins, or the board is full without space for another move hence resulting in a tie. 

## Why MinMax?

Minmax is an artificial intelligence commonly applied to 2 player games, since by nature the algorithm assumes that two parties are working towards opposite goals. Games such as Chess, Checkers, Connect Four, and Tic-Tac-Toe are zero-sum games where there is one winner, denoted as (+1), one loser (-1) and in some cases a tie (0). 
Additionally, Tic-Tac-Toe, Checkers and Connect Four are all solved games. A solved game in this context is a game in which the outcome (win loss or tie) can be predicted from any position, assuming that both players are playing optimally. Some games are simple to solved like Tic-Tac-Toe and others are very hard to solve like checkers; being solved in 2007 after a 19-year project. To put that into context Tic-Tac-Toe was solved in 1980. 
Due to Tic-Tac-Toe’s simplicity, a full game of Tic-Tac-Toe can be mapped out on a tree with only 549,946 nodes making the Minmax algorithm suitable for the scope of this project. More complex games with higher levels of depth, such as Chess which have around 10100 (10 followed by 100 zeros) nodes making calculating the next moved expensive, time and space wise. For these kinds of problems, we could use Alpha-Beta Pruning, which allows us to cut of certain branches of our tree that we deem unsuitable while it searches for a solution.  

## Implementation

# opp_MinMax

![Screenshot 2024-02-03 154730](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/3ac56739-52ef-4147-bc80-39e2a3381075)

This block is the foundation for the minmax algorithm. First, we initialize the AI’s score as -100. This is an arbitrary number; since the AI is maximizing, the worst score the AI could get would be the initial value. I could have imported the inf from the math library but I decided that -100 would function the same and save on space. 
After, we initialize the bestMove as 0,0. The two variables represent row and column respectively, since I will be displaying this on my button grid of my GUI. Finally, we take a snapshot of the board using the boardState() function I will go over bellow, calling it board for simplicity. 
Once all the necessary variables are initialized, we begin the minmax for loop. This works by taking the index and the char from the board array and checking whether its empty. If its empty, then we change it to the opposing character (the one the player didn’t choose in the character selection screen) and call minmax(). 
Minmax takes in board and a boolean value called isMaximizing; returning a score based on the success of that move. IsMaximizing is used to determine which players turn is it. As mentioned before, the algorithm assumes that two parties are working towards opposite goals, and it’s the AI job to maximize its score while minimizing the opponents score, the human player. We have it as false because it would be the human player’s turn. 
After a score has been returned, it reverts the board back to how it was at the start, and then compares the new score with the bestScore. If it finds that the new score is greater, it saves that move as bestMove and that score as bestScore. After the AI has gone over every available space, the best move will then be displayed on the button grid by passing the variable to insertOppVal.

# Minmax algorithm

![Screenshot 2024-02-03 154754](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/389fd1ad-044a-422b-80d6-e9e050a8aead)

Firstly, we check if the game as concluded by checking if a player has won or if there are no placed left of the board. If the game is still on, IsMaximizing will determine the next move. The code inside the if statements resembles the previous segment, since is a recursive algorithm. In this instance, Opp_minmax is the parent node and the minmax method is generating all the possible children and returning 1,-1, or 0 depending on how the game ends. 
Notice that when it isn’t maximizing or minimizing it is flipped. Instead of bestScore being -100, its 100 and if the score is less than bestScore then we would update the bestScore variable. 

#CheckWhoWin and checkDraw

![Screenshot 2024-02-03 154808](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/a7e2660f-bb52-4061-952f-584013172c94)

This algorithm takes in the board and a player char. For this I found it simple to use a 2D array filled with all the possible win conditions and then iterated through the array and compare each position to the player char. If a player meets the requirements for the win condition, then it returns true. This allows for cleaner code instead of just listing out a bunch of if statements making it easier to debug. 
checkDraw takes an input the board and checks if there are no empty spaces left, denoted by the ‘0’

#BestMoveConverstion

![Screenshot 2024-02-03 154922](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/2e2c6269-fe01-42ad-810f-7bedd6bdb2d6)

I noticed that for my grid of 3x3 I could use a simple division and mod to get the exact coordinates to display on the GUI. The reason I have them as two variables instead of just putting them together with the return was for readability and debugging. While more efficient it could be confusing if someone wanted to build upon my code. 

#Color Use 
I intentionally used color to provide my player with a more user-friendly experience and to express with color what each of the button do. Some of these are typical conventions such as: 
Green : Start 
Red : Return
Different colors based on the difficult chosen, which also go with the color pallet of the project, this was to ensure that the user has chosen the right one. I also wrote at the top which algorithm was used but wanted a way to express that visually to the player as to promote intuition. 
Furthermore, green was chosen as the player character, not only because this shade of green symbolizes nature and life, as the human player, but also because the two colors adjacent to it on the color wheel are yellow and blue. These analogous colors add to the visual appeal and my visual style which is not too contrasty. 

![Screenshot 2024-01-30 135621](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/92e9875f-c0d5-40f7-a75c-116c3f8ee572) ![Screenshot 2024-01-30 135633](https://github.com/arisocorro/TicTacToeGUI/assets/158087556/f820a91e-25a1-42e9-be02-eb6d569abc82)
