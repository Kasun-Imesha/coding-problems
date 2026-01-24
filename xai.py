import numpy as np

figures_dict = {
    "A": [[1]],
    "B": [[1,1,1]],
    "C": [[1,1], [1,1]],
    "D": [[1,0], [1,1], [1,0]],
    "E": [[0,1,0], [1,1,1]]
}

shapes_dict = {}

for k in figures_dict:
    figures_dict[k] = np.array(figures_dict[k])
    shapes_dict[k] = figures_dict[k].shape

print(figures_dict)
print(shapes_dict)

n = 5
m = 4
figures = ["E", "D", "C", "A"]
grid = np.zeros((n, m), dtype=np.int32)
w = 0
h = 0

for k, figure_k in enumerate(figures):
    figure = figures_dict[figure_k]
    fh, fw = shapes_dict[figure_k]

    done = False
    for i in range(n):
        if i + fh > n:
            continue
        
        for j in range(m):
            if j + fw > m:
                continue

            patch = grid[i:i+fh, j:j+fw]

            if np.sum(patch * figure) == 0: 
                grid[i:i+fh, j:j+fw] += figure * (k + 1)
                done = True
                break
            
        if done:
            break

print(grid)
