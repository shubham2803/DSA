# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
import random


class RandomizedSet:

    def __init__(self):
        self.items = {}
        self.item_list = []

    def insert(self, val: int) -> bool:
        if val not in self.items:
            self.items[val] = len(self.item_list)
            self.item_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.items:
            idx = self.items.get(val)
            last_value = self.item_list[-1]
            self.item_list[idx] = self.item_list[-1]
            self.items[last_value] = idx
            self.items.pop(val)

            self.item_list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.item_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
