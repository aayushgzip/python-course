def count_island(grid):
    rows = len(grid)
    cols = len(grid[0])
    num_island = 0
    def dfs(x,y):
        stack = [(x,y)]
        while stack:
            ci, cj = stack.pop()
            if 0<=ci<rows and 0<=cj<cols and grid[ci][cj]==1:
                grid[ci][cj]=-1
                stack.extend([(ci-1,cj),(ci+1,cj),(ci,cj-1),(ci,cj+1)])
            

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                num_island+=1
                dfs(i,j)
    return num_island
islands = [ list(map(int, "1100000111")),
    list(map(int, "1000000111")),
    list(map(int, "0000000111")),
    list(map(int, "0010001000")),
    list(map(int, "0000011100")),
    list(map(int, "0000111110")),
    list(map(int, "0001111111")),
    list(map(int, "1000111110")),
    list(map(int, "1100011100")),
    list(map(int, "1110001000"))]
num_islands = count_island(islands)
print("number of islands are : ",num_islands)
