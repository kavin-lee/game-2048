"""
    数据模型类
"""
from enum import Enum
from enum import unique


class Location:
    def __init__(self, i, n):
        self.i__index = i
        self.n__index = n

    @property
    def i__index(self):
        return self.__i__index

    @i__index.setter
    def i__index(self, value):
        self.__i__index = value

    @property
    def n__index(self):
        return self.__n__index

    @n__index.setter
    def n__index(self, value):
        self.__n__index = value


#使用枚举模块
@unique
class Direction(Enum):
    up = 0
    down = 1
    left = 2
    right = 3
