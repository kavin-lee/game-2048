"""
    界面视图类
"""

from bll import GameCoreController
from model import Direction
import os


class Game2048View:

    def __init__(self):
        self.__control = GameCoreController()

    def print_map(self):
        os.system("clear")
        for i in range(len(self.__control.map)):
            for n in range(len(self.__control.map[i])):
                print("%4s" % self.__control.map[i][n], end=" ")
            print()
            print()
        print("得分:%d".center(22)%self.__control.total_score)
        print()
    def start(self):
        self.__control.generat_random_new_number()
        self.__control.generat_random_new_number()
        self.print_map()

    def move_map(self):
        """
        方向选择
        :return:
        """
        direction = input("请输入(w-s-a-d)选择移动方向:")
        if direction == "w":
            self.__control.move(Direction.up)
        elif direction == "s":
            self.__control.move(Direction.down)
        elif direction == "a":
            self.__control.move(Direction.left)
        elif direction == "d":
            self.__control.move(Direction.right)

    def update(self):
        while True:
            self.move_map()
            if self.__control.is_change:
                self.__control.generat_random_new_number()
                self.print_map()
                if self.__control.is_game_over():
                    print("Game Over")
                    break