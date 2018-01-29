#55.py

intervals = [[1,3],[2,6],[8,10],[15,18]]
i,j = 0,0
def merge1(intervals,i,j):
    while i<len(intervals)-1:
        if intervals[i][j+1]<intervals[i+1][j]:
            i+=1
            return merge1(intervals,i,j)
        else:
            intervals[i][j+1] = intervals[i+1][j+1]
            intervals = intervals[:i+1]+intervals[i+2:]
            return merge1(intervals,i,j)
    return intervals
print merge1(intervals,i,j)