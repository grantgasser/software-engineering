# Mountain Rainfall
# Overview

# We want to write a program that determines the steady-state collection points of rain falling on mountainous terrain.

# In this scenario, one centimeter of rain falls uniformly across the terrain. Water flows downhill until it reaches a local minimum. The total accumulation of water in any location is negligible compared to the height of the terrain.
# Input Specification

# You receive a 2-dimensional array (of dimension n by m) containing non-negative integers. The integer at position  (x,y) in the array represents the elevation (in kilometers) of the terrain at position (x,y).

# Sample Input:

# [ 
#   [3, 3, 1, 0],
#   [2, 3, 3, 2],  
#   [0, 1, 3, 3]
# ]

# In this sample, the height at position (1, 1) is 3 kilometers, n=3 and m=4.
# Output Specification

# An n by m array of non-negative integers, where the integer at position (x,y)represents the amount of rain that has accumulated at that location.

# Sample output:

# [ 
#   [0, 0, 0, 6],
#   [0, 0, 0, 0],
#   [6, 0, 0, 0]
# ]

"""
# [ 
#   [0, 0, 0, 2],
#   [1, 0, 0, 0],
#   [0, 0, 0, 0]
# ]


O((mxn))
"""


# initialize nxm result matrix w/ 0s
# 
# for given cell, look adjacent cells
	# find index of min(adj_cells); find min_i, min_j
  # if min exists:
  	# add arr[min_i][min_j] = arr[i][j] + 1
    
  # else:
  	# arr[i][j] += 1
import numpy as np

def get_water_steady_state(terrain_matrix):
  steady_state_matrix = [[0 for i in range(len(terrain_matrix[0]))] for j in range(len(terrain_matrix))]
  min_index_of_adj_neighbors = [[(-1, -1) for i in range(len(terrain_matrix[0]))] for j in range(len(terrain_matrix))]  # store tupls of min idx
  
  for i in range(len(terrain_matrix)):
    for j in range(len(terrain_matrix[0])):
      curr_i = i
      curr_j = j
        
      # Once we know min of neighbors, go there unless we're already at min
      while (curr_i != min_index_of_adj_neighbors[curr_i][curr_j][0] and curr_j != min_index_of_adj_neighbors[curr_i][curr_j][1]):
        # If we haven't already computed min for this cell
        if min_index_of_adj_neighbors[curr_i][curr_j] == (-1, -1):
          # Get min of neighbors
          min_index_of_adj_neighbors[curr_i][curr_j] = get_min_neighbor_index(curr_i, curr_j, terrain_matrix)        	
				
        # Update current as we're moving along cells
        prev_i = curr_i
        curr_i = min_index_of_adj_neighbors[curr_i][curr_j][0]
        curr_j = min_index_of_adj_neighbors[prev_i][curr_j][1] 
      

      # Update in special case (REFACTOR)
      prev_i = curr_i
      curr_i = min_index_of_adj_neighbors[curr_i][curr_j][0]
      curr_j = min_index_of_adj_neighbors[prev_i][curr_j][1]
      
      # Now we're at the min, add
      steady_state_matrix[curr_i][curr_j] += 1
      
  return steady_state_matrix, min_index_of_adj_neighbors
        

"""
Returns tuple representing index of the min neighbor of cell i,j
"""
def get_min_neighbor_index(i, j, terrain_matrix):
  min_val = float('inf')
  min_idx = (-1, -1)
  for new_i in range(i-1, i+2):
    if new_i >= 0 and new_i <= len(terrain_matrix) - 1:
      for new_j in range(j-1, j+2):
        if new_j >= 0 and new_j <= len(terrain_matrix[0]) - 1:
          if terrain_matrix[new_i][new_j] < min_val:
            min_val = terrain_matrix[new_i][new_j]
            min_idx = (new_i, new_j)
            
  return min_idx
    
  
"""
TESTING
"""
arr = [ 
  [3, 3, 1, 0],
  [2, 3, 3, 2],  
  [0, 1, 3, 3]
]

  
get_min_neighbor_index(1,1,arr)  # => (2, 0)
get_min_neighbor_index(0,2,arr)  # => (0, 3)
get_min_neighbor_index(2,2,arr)  # => (2, 1)


get_water_steady_state(arr)  # => returns answer
  


