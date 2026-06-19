# Core DFS-Backtracking Engine
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(r, c, next_req):
    # Terminal Condition: All cells visited and max waypoint reached
    if len(path) == (n * n):
        return grid[r][c] == max_wp

    # Explore 4 orthogonal directions without conditional branching
    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc
        
        # O(1) Constraint Validation: Boundaries and Visitation
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            cell = grid[nr][nc]
            
            # Sequence Validation for Waypoint Cells
            if cell > 0 and cell != next_req:
                continue # Prune: Invalid ordering
            
            # Determine next required waypoint
            nxt = (next_req + 1) if (cell > 0 and next_req < max_wp) else next_req
            
            # In-Place State Mutation
            visited[nr][nc] = True
            path.append((nr, nc))
            
            # Recursive Dive
            if dfs(nr, nc, nxt):
                return True
                
            # In-Place State Restoration (Backtracking)
            path.pop()
            visited[nr][nc] = False

    return False