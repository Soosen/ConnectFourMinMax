import arcade
import sys
import pyglet
import time
import math
from connectFour import ConnectFour
from connectFourAI import ConnectFourAI


GRID_WIDTH = 7
GRID_HEIGHT = 6
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * GRID_HEIGHT/GRID_WIDTH)
SCREEN_TITLE = "Connect Four Min Max"

#fps
UPDATE_RATE = 1/60

#chosen Monitor
MONITOR_NUM = 0
MONITORS = pyglet.canvas.Display().get_screens()
MONITOR = MONITORS[MONITOR_NUM]



class MyProject(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLUE)

    def setup(self):

        #increase recursion limit
        sys.setrecursionlimit(30000)

        #set fps
        self.set_update_rate(UPDATE_RATE)

        #center the window on start
        self.center_on_screen()

        self.c4 = ConnectFour(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_WIDTH, GRID_HEIGHT)
        self.c4AI = ConnectFourAI(self.c4)
        self.end = False
        pass

    def on_draw(self):
        #draw the maze
        self.clear()
        arcade.start_render()
        self.c4.draw()
        arcade.finish_render()


    def on_update(self, delta_time):
        if(not self.end):
            won, player = self.c4.isEnd(self.c4.state)
            if(won):
                print("Player ",player , " won")
                self.end = True
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        if(button == arcade.MOUSE_BUTTON_RIGHT):
            if(not self.end):
                bestColumn = self.c4AI.getBestMove(self.c4.state, 3, 1)
                self.c4.state = self.c4.insertToken(bestColumn, self.c4.state, self.c4.player)
                self.c4.player = self.c4.changePlayer(self.c4.player)
        else:
            if(not self.end):
                column = math.floor(x/(SCREEN_WIDTH/GRID_WIDTH))
                self.c4.state = self.c4.insertToken(column, self.c4.state, self.c4.player)
                self.c4.player = self.c4.changePlayer(self.c4.player)
        
                
        pass

    def on_key_press(self, key, key_modifiers):

        #Key R - generate new sudoku board
        if key == arcade.key.R:
            self.c4.reset()
            self.end = False
        elif key == arcade.key.S:
            print("S")
       
        pass

    def center_on_screen(self):
        _left = MONITOR.width // 2 - self.width // 2
        _top = (MONITOR.height // 2 - self.height // 2)
        self.set_location(_left, _top)

def main():
    project = MyProject(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    project.setup()

    arcade.run()




if __name__ == "__main__":
    main()