import time

def solve_zip(grid):
    n = len(grid)
    max_wp = 0
    start = (0, 0)

    # 1. Pre-processing: Cari posisi '1' dan k (max_wp)
    for r in range(n):
        for c in range(n):
            if grid[r][c] > max_wp:
                max_wp = grid[r][c]
            if grid[r][c] == 1:
                start = (r, c)

    visited = [[False] * n for _ in range(n)]
    path = [start]
    visited[start[0]][start[1]] = True
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Counter untuk menghitung jumlah state (node) yang dievaluasi
    cells_explored = [0]

    # 2. Core DFS-Backtracking Engine
    def dfs(r, c, next_req):
        cells_explored[0] += 1 # Tambah counter setiap evaluasi node
        
        # Base case: ukuran path sudah n*n
        if len(path) == n * n:
            return grid[r][c] == max_wp

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            # Constraint Validation
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                cell = grid[nr][nc]
                
                # Pruning: Waypoint salah urutan
                if cell > 0 and cell != next_req:
                    continue 
                
                nxt = (next_req + 1) if (cell > 0 and next_req < max_wp) else next_req
                
                # In-Place State Mutation
                visited[nr][nc] = True
                path.append((nr, nc))
                
                # Recursive Descent
                if dfs(nr, nc, nxt):
                    return True
                    
                # In-Place State Restoration (Backtrack)
                path.pop()
                visited[nr][nc] = False

        return False

    # 3. Execution & High-Precision Timing
    t0 = time.perf_counter()
    is_found = dfs(start[0], start[1], 2)
    t1 = time.perf_counter()

    time_ms = (t1 - t0) * 1000 # Konversi ke milidetik

    return path if is_found else None, cells_explored[0], time_ms, max_wp

# ==========================================
# BLOK MAIN (CLI INTERAKTIF UNTUK EKSPERIMEN)
# ==========================================
if __name__ == "__main__":
    print("========================================")
    print("  ZIP SOLVER: EXPERIMENT & BENCHMARK    ")
    print("========================================\n")

    try:
        # Input ukuran grid
        n_input = int(input("Masukkan ukuran papan (n): "))
        
        print(f"Masukkan {n_input} baris angka (pisahkan dengan spasi, gunakan 0 untuk petak kosong):")
        
        # Membaca grid dari input terminal
        grid_dynamic = []
        for i in range(n_input):
            row = list(map(int, input().split()))
            if len(row) != n_input:
                print(f"❌ Error: Baris {i+1} tidak memiliki tepat {n_input} angka. Program dihentikan.")
                exit()
            grid_dynamic.append(row)

        print("\n⚙️  Executing DFS-Backtracking Engine...\n")
        
        # Jalankan solver
        solution, explored, time_ms, waypoints = solve_zip(grid_dynamic)
        
        # Cetak metrik eksperimen untuk Tabel Jurnal
        print("========================================")
        print("          EXPERIMENTAL RESULTS          ")
        print("========================================")
        print(f"Grid Size      : {n_input}x{n_input}")
        print(f"Waypoints (k)  : {waypoints}")
        print(f"Cells Explored : {explored:,} states")
        print(f"Time Elapsed   : {time_ms:.3f} ms")
        
        # Cetak status dan langkah jika ditemukan
        if solution:
            print(f"Solution Found : Yes (Path length: {len(solution)})")
            print("-" * 40)
            print("Path sequence:")
            for step, (r, c) in enumerate(solution):
                print(f"  Step {step + 1:02d}: Go to ({r}, {c})")
        else:
            print(f"Solution Found : No (Infeasible Configuration)")
        print("========================================")

    except ValueError:
        print("\n❌ Error: Input tidak valid. Pastikan Anda hanya memasukkan angka (integer).")