def solve_zip(grid):
    n = len(grid)

    # O(n^2) preprocessing: locate all waypoints
    waypoints = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                waypoints[grid[i][j]] = (i, j)

    max_wp = max(waypoints.keys())
    start  = waypoints[1]