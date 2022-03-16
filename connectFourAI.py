MAX_WINNING_SCORE = 999999
MIN_WINNING_SCORE = -999999
MAXIMIZING_PLAYER_ID = 1
MINIMIZING_PLAYER_ID = 2

class ConnectFourAI:
    def __init__(self, connectFour):
        self.connectFour = connectFour
        self.gridWidth = self.connectFour.gridWidth
        self.gridHeight = self.connectFour.gridHeight
        return

    def calculateScore(self, state):
        horizontalPoints = 0
        verticalPoints = 0
        diagonalPointsRight = 0
        diagonalPointsLeft = 0

        for i in range(self.connectFour.gridWidth - 3):
            for j in range(self.connectFour.gridHeight):
                tempPoints = self.calculateScorePosition(i, j, state, 1, 0)
                horizontalPoints += tempPoints

        
        for i in range(self.connectFour.gridWidth):
            for j in range(self.connectFour.gridHeight - 3):
                tempPoints = self.calculateScorePosition(i, j, state, 0, 1)
                verticalPoints += tempPoints

        for i in range(self.connectFour.gridWidth - 3):
            for j in range(self.connectFour.gridHeight - 3):
                tempPoints = self.calculateScorePosition(i, j, state, 1, 1)
                diagonalPointsRight += tempPoints

        for i in range(self.connectFour.gridWidth - 3):
            for j in range(self.connectFour.gridHeight - 3):
                tempPoints = self.calculateScorePosition(i + 3, j, state, -1, 1)
                diagonalPointsLeft += tempPoints


        return  horizontalPoints + verticalPoints + diagonalPointsRight + diagonalPointsLeft
    
    def calculateScorePosition(self, x, y, state, incrementX, incrementY):

        playerPoints = 0
        aiPoints = 0

        for i in range(4):
            if(state[x][y] == MINIMIZING_PLAYER_ID):
                playerPoints += 1

            elif(state[x][y] == MAXIMIZING_PLAYER_ID):
                aiPoints += 1
            
            x += incrementX
            y += incrementY
        
        if(playerPoints == 4):
            return MIN_WINNING_SCORE
        
        elif(aiPoints == 4):
            return MAX_WINNING_SCORE
        
        else:
            return aiPoints

    def minimax(self, state, depth, alpha, beta, maximizingPlayer):
        end, player =  self.connectFour.isEnd(state)
        if(depth == 0 or end):
            return self.calculateScore(state)

        print(depth)

        if(maximizingPlayer):
            maxEval = MIN_WINNING_SCORE
            neigh = self.connectFour.generateNeighbourStates(state, MAXIMIZING_PLAYER_ID)

            for n in neigh:
                eval = self.minimax(n.state, depth - 1, alpha, beta, False)  
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)

                if(beta <= alpha):
                    break

            return maxEval

        else:
            minEval = MAX_WINNING_SCORE
            neigh = self.connectFour.generateNeighbourStates(state, MINIMIZING_PLAYER_ID)
            for n in neigh:
                eval = self.minimax(n.state, depth - 1, alpha, beta, True)    
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if(beta <= alpha):
                    break
            
            return minEval

    def getBestMove(self, state, maxDepth, maximizingPlayerID):
        neigh = self.connectFour.generateNeighbourStates(state, maximizingPlayerID)
        bestScore = MIN_WINNING_SCORE
        bestColumn = -1

        for n in neigh:
            tempScore = self.minimax(n.state, maxDepth, MIN_WINNING_SCORE, MAX_WINNING_SCORE, True)
            if(tempScore >= bestScore):
                bestColumn = n.column
                bestScore = tempScore
        
        return bestColumn