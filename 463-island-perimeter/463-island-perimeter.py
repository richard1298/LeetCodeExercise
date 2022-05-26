class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perim = 0
        for i in range(row):
            side = 0
            updown = 0
            for j in range(col):
                if i ==0 :
                    #upper edge of the first row
                    if grid[i][j]:updown += 1
                else:
                    if (grid[i][j] + grid[i-1][j] ==1):updown += 1 
                if i == row -1 and grid[i][j]:
                    #lower edge of the last row
                    updown += 1
                if j ==0:
                    #left edge of the first row 
                    if grid[i][j]:side += 1
                else:
                    if (grid[i][j] + grid[i][j-1]==1):side+=1 
                if j == col-1 and grid[i][j]:
                    side+=1
            perim += updown + side
            #print('up down edge of row',i,'is',updown)
            #print('side edge of row',j,'is',side)
        return perim
                    
                    
                        
                
                    