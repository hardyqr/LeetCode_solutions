# Freddy/Fangyu
# 12/11/2016

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count=0

        h_length=len(board)
        w_length=len(board[0])
        # print(h_length,w_length)
        if h_length==0 or w_length==0:
            return count
        else:
            for x in range(1,h_length):
                if board[x][0]=='X' and board[x-1][0]!='X':
                    count+=1
            for y in range(1,w_length):
                if board[0][y]=='X' and board[0][y-1]!='X':
                    count+=1

            if board[0][0]=='X':count+=1

            for x in range(1,h_length):
                for y in range(1,w_length):
                    if board[x][y]=='X' and board[x-1][y]!='X' and board[x][y-1]!='X':
                        count+=1
            # print(count)
            return count

    # countBattleships(object,["X..X","...X","...X"])
    # countBattleships(object,[''])
    # countBattleships(object,["X"])
    # countBattleships(object,["XXX"])
