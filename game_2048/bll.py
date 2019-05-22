"""
    游戏核心类
"""
import random
from model import Location
from model import Direction
import math
import copy


class GameCoreController:
    """
        游戏核心控制器
    """

    def __init__(self):
        self.__map = [
            [0] * 4,
            [0] * 4,
            [0] * 4,
            [0] * 4
        ]
        self.__list_merge = []
        self.__list_empty_zero = []
        self.is_change = False
        self.total_score=0

    @property
    def map(self):
        return self.__map

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
            合并相同
        :return:
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
                self.total_score+=self.__list_merge[i]
        self.__zero_to_end()

    def __move_left(self):
        """
            向左移动
        :return:
        """
        for i in range(len(self.__map)):
            self.__list_merge[:] = self.__map[i]
            self.__merge()
            self.__map[i][:] = self.__list_merge

    def __move_right(self):
        """
            向右移动
        :return:
        """
        for i in range(len(self.__map)):
            self.__list_merge = self.__map[i][::-1]
            self.__merge()
            self.__map[i][::-1] = self.__list_merge

    def __move_up(self):
        """
            向上移动
        :return:
        """
        for i in range(len(self.__map)):
            self.__list_merge.clear()
            for n in range(len(self.__map[i])):
                self.__list_merge.append(self.__map[n][i])
            self.__merge()
            for n in range(len(self.__map)):
                self.__map[n][i] = self.__list_merge[n]

    def __move_down(self):
        """
            向下移动
        :return:
        """
        for i in range(len(self.__map)):
            self.__list_merge.clear()
            for n in range(len(self.__map[i]) - 1, -1, -1):
                self.__list_merge.append(self.__map[n][i])
            self.__merge()
            for n in range(len(self.__map) - 1, -1, -1):
                self.__map[n][i] = self.__list_merge[len(self.__map) - 1 - n]

    def __get_list_map_zero(self):
        """
            获取所有的零元素位置
        :return:
        """
        self.__list_empty_zero.clear()
        for i in range(len(self.__map)):
            for n in range(len(self.__map[i])):
                if self.__map[i][n] == 0:
                    loc = Location(i, n)
                    self.__list_empty_zero.append(loc)

    def generat_random_new_number(self):
        """
            产生新的随机数,删除占用的位置
        :return:
        """
        self.__get_list_map_zero()
        if len(self.__list_empty_zero) == 0:
            return
        loc = random.choice(self.__list_empty_zero)
        self.__map[loc.i__index][loc.n__index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_zero.remove(loc)


    def move(self, dir):
        """
            包装移动,并且判断移动前后元素是否相同
        :param dir:
        :return:
        """
        # self.is_change = False
        original_map = copy.deepcopy(self.__map)
        if dir == Direction(0):
            self.__move_up()
        elif dir == Direction(1):
            self.__move_down()
        elif dir == Direction(2):
            self.__move_left()
        elif dir == Direction(3):
            self.__move_right()
        self.is_change = original_map != self.__map

    # def __equal_map(self, original):
    #     for i in range(len(original)):
    #         for n in range(len(original[i])):
    #             if original[i][n] != self.__map[i][n]:
    #                 return True
    #     return False

    def is_game_over(self):
        """
            判断游戏是否结束
        :return: bool值
        """
        if len(self.__list_empty_zero) > 0:
            return False
        for i in range(len(self.__map)):
            for n in range(len(self.__map[i]) - 1):
                if self.__map[i][n] == self.__map[i][n + 1] or self.__map[n][i] == self.__map[n + 1][i]:
                    return False
        return True
