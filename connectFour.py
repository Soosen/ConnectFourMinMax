import numpy
import arcade

class ConnectFour:
    def __init__(self, w,  h, gw, gh):
        self.player = 1
        self.width = w
        self.height = h
        self.gridWidth = gw
        self.gridHeight = gh
        self.state = numpy.zeros(shape = (self.gridWidth, self.gridHeight), dtype=int)
        self.tileWidth = self.width/gw
        self.tileHeight = self.height/gh
    

    def insertToken(self, x, state, player):
        copyState = numpy.copy(state)
        for i in range (state[x].size):
            if(copyState[x][i] == 0):
                copyState[x][i] =  player
                return copyState
        
        return copyState

    def changePlayer(self, player):
        return player % 2 + 1

    
    def isEnd(self, state):

        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                cur = state[j][i]
                if(cur == 0):
                    continue

                if(i < self.gridHeight - 3 and state[j][i + 1] == cur and state[j][i + 2] == cur and state[j][i + 3] == cur):
                    return True, cur
                
                if(j < self.gridWidth - 3 and state[j + 1][i] == cur and state[j + 2][i] == cur and state[j + 3][i] == cur):
                    return True, cur
                
                if(i < self.gridHeight - 3 and j < self.gridWidth - 3 and state[j + 1][i + 1] == cur and state[j + 2][i + 2] == cur and state[j + 3][i + 3] == cur):
                    return True, cur
                
                if(i < self.gridHeight - 3 and j >= 3 and state[j - 1][i + 1] == cur and state[j - 2][i + 2] == cur and state[j - 3][i + 3] == cur):
                    return True, cur

        return False, None

    def reset(self):
        self.state = numpy.zeros(shape = (self.gridWidth, self.gridHeight), dtype=int)

    def generateNeighbourStates(self, state, player):
        neigh = numpy.array([])
        for i in range(self.gridWidth):
            if(state[i][self.gridHeight - 1] == 0):
                neigh = numpy.append(neigh, Neighbour(self.insertToken(i, state, player), i))

        return neigh


    def draw(self):
        for i in range(self.gridHeight):
            #horizontal
            arcade.draw_line(0, i * self.tileHeight, self.width, i * self.tileHeight, arcade.color.BLACK, 3)

        for i in range(self.gridWidth):
            #vertical
            arcade.draw_line(i * self.tileWidth, 0, i * self.tileWidth , self.height, arcade.color.BLACK, 3)

        for i in range(self.gridWidth):
            for j in range(self.gridHeight):
                color = arcade.color.WHITE
                if(self.state[i][j] == 1):
                    color = arcade.color.YELLOW
                elif(self.state[i][j] == 2):
                    color = arcade.color.RED

                arcade.draw_circle_filled((i + 0.5) * self.tileWidth, (j + 0.5) * self.tileHeight, self.tileHeight/4, color)

class Neighbour():
    def __init__(self, state, column):
        self.state = state
        self.column = column