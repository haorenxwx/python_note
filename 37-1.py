class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return 
        self.solve(board)
    
    def solve(self, board):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == '.':
                    for c in "1234567879":
                        if self.isValid(board,i,j,c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True
                            
    def isValid(self,board,x,y,c):

        for i in xrange(9):
            if board[i][y] == c:
                return False
        for j in xrange(9):
            if board[x][j] == c:
                return False
        for i in xrange(3):
            for j in xrange(3):
                if board[(x/3)*3+i][(y/3)*3+j] == c:
                    return False
        
        return True