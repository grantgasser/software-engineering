import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.ndimage import generic_filter

"""
Context: 
  - https://en.wikipedia.org/wiki/Schelling%27s_model_of_segregation
  - http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/

"""
class SchellingBoard:
    def __init__(self, n, thresh, empty=0.1, black=0.25, white=0.65):
        """
        Creates a board representing a neighborhood and initializes dynamics of environment

        n: number of rows and cols
        thresh: minimum number of neighbors of its same group the agent prefers to have
        empty: % of cells (lots) that are empty
        black: % of cells (lots) occupied by black
        white: % of cells (lots) occupied by white
        """
        self.n = n
        self.thresh = thresh
        self.empty = empty
        self.black = black
        self.white = white

        # create the board
        self.board = np.random.choice([0, 1, 2], size=(n, n), p=[black, empty, white])
        self.initial_board = self.board.copy()  # keep for comparison

    def plot(self, i, initial=False, self_close=True):
        if initial:
            board = self.initial_board
            i = 'INITIAL'
        else:
            board = self.board

        plt.figure(figsize=(12, 10))
        plt.imshow(board, cmap='binary_r')
        plt.xticks([])
        plt.yticks([])
        plt.title(
            f"Neighborhood (threshold: {self.thresh:.2%}, black: {self.black:.2%}, white: {self.white:.2%}); Month: {i}",
            fontsize=20
        )

        plt.draw()
        if i == 0:
            plt.pause(3)
        else:
            plt.pause(1)
        plt.clf()

        if self_close:
            plt.close()

    def update(self):
        for i in range(self.n):
            for j in range(self.n):
                neighbor_homo = self.check_neighbors(i,j)

                if neighbor_homo < self.thresh:
                    #print(f'i={i}, j={j} is unhappy with {neighbor_homo}')

                    # Move an unhappy agent to an empty cell / lot
                    move_to_i, move_to_j = self.find_empty()
                    self.board[move_to_i, move_to_j] = self.board[i, j]
                    self.board[i, j] = 1

                else:
                    pass
                    #print(f'i={i}, j={j} is HAPPY with {neighbor_homo}')

    def check_neighbors(self, i, j):
        """
        Checks the agent's neighbors and returns `l`, the % of same neighbors
        
        `l` indicates whether or not the agent remains or 
        """
        same_neighbors = 0
        total_neighbors = 0

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                # don't count the cell itself as a neighbor
                if di == 0 and dj == 0:
                    continue

                # calculate the index of the neighbor
                ni = i + di
                nj = j + dj

                # make sure the neighbor is within the bounds of the array
                if ni >= 0 and ni < self.n and nj >= 0 and nj < self.n:
                    total_neighbors += 1
                    # count the neighbor if it has the same value
                    if self.board[ni, nj] == self.board[i, j]:
                        same_neighbors += 1

        return same_neighbors / total_neighbors
    
    def find_empty(self):
        """Finds a random empty cell in the grid / empty lot in the neighborhood"""
        indices_of_ones = np.argwhere(self.board == 1)
        index_of_index = np.random.choice(indices_of_ones.shape[0])
        i, j = indices_of_ones[index_of_index]

        return i,j
        
# Get user input for simulation
months = int(input('How many months should we simulate?: '))
thresh = float(input('What percentage of neighbors should people desire to be like themselves? (ex: `0.4` as 40%): '))

# Create board and run simulation
board = SchellingBoard(30, thresh)
for i in range(months):
    board.update()
    board.plot(i)

# Compare initial board to final board
board.plot(i=0, initial=True, self_close=False)
plt.show()
board.plot(i=months, self_close=False)
plt.show()