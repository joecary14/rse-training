import numpy as np

def step(grid):
    grid_copy = grid.copy()
    rows, cols = grid_copy.shape
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(grid_copy, i, j)
            count = sum(neighbors)
            if grid_copy[i, j] == 1:
                if count in [2, 3]:
                    grid_copy[i, j] = 1
            elif count == 3:
                grid_copy[i, j] = 1
                
    return grid_copy


def get_neighbors(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 0, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)
step(grid)
print(grid)  # should be unchanged, but may change due to the bug