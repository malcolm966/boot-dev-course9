from user import *

class HashMap:

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None:
            # 找到 key
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]

            # 已经绕了一圈
            if not first_iteration and index == original_index:
                raise Exception("sorry, key not found")

            # 线性探测
            index = (index + 1) % len(self.hashmap)
            first_iteration = False

        # 遇到 None，说明不存在
        raise Exception("sorry, key not found")

    def insert(self, key, value):
        # resize（按你已有逻辑）
        self.resize()

        index = self.key_to_index(key)
        original_index = index
        first_iteration = True

        while self.hashmap[index] is not None and self.hashmap[index][0] != key:
            # 已经绕了一圈，表满
            if not first_iteration and index == original_index:
                raise Exception("hashmap is full")

            index = (index + 1) % len(self.hashmap)
            first_iteration = False

        # 插入或覆盖
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return
        hashmap_load = self.current_load()
        if hashmap_load < 0.05:
            return
        else:
            temp = self.hashmap
            self.hashmap = [None for i in range(10 * len(temp))]
            for item in temp:
                if item is not None:
                    index = self.key_to_index(item[0])
                    self.hashmap[index] = item

    def current_load(self):
        ele_count = 0
        for i in self.hashmap:
            if i is not None:
                ele_count += 1
        if ele_count == 0:
            return 1
        return ele_count / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
