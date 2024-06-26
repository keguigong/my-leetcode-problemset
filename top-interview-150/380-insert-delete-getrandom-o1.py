# 380. O(1) 时间插入、删除和获取随机元素
# https://leetcode.cn/problems/insert-delete-getrandom-o1/

from random import choice


class RandomizedSet:
    def __init__(self):
        self.lookup = dict()
        self.data = []

    def insert(self, val: int) -> bool:
        if val not in self.lookup:
            self.lookup[val] = len(self.data)
            self.data.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.lookup:
            i = self.lookup[val]
            self.data[i] = self.data[-1]
            self.lookup[self.data[i]] = i
            self.data.pop()
            del self.lookup[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
