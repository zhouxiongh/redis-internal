from collections import OrderedDict

class LRUDict(OrderedDict):
    """docstring for LRUDict"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = OrderedDict()

    def __setitem__(self, key, value):
        old_val = self.items.get(key)
        if old_val:
            self.items.pop(key)
        elif len(self.items) >= self.capacity:
            self.items.popitem(last=True)
        self.items[key] = value


    def __getitem__(self, key):
        val = self.items.get(key)
        if val:
            self.items.pop(key)
            self.items[key] = val
        return val

    def __repr__(self):
        return repr(self.items)


d = LRUDict(10)

for i in range(15):
    d[i] = i
print(d)

