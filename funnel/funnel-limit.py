import time

class Funnel(object):
    """dcapacity, leaking_ratetring for Funnel"""
    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity
        self.leaking_rate = leaking_rate
        self.left_quata = capacity
        self.leaking_ts = time.time()

    def make_sapce(self):
        now_ts = time.time()
        delta_ts = now_ts - self.leaking_ts
        delta_quata = delta_ts * self.leaking_rate
        if delta_quata < 1:
            return
        self.left_quata += delta_quata
        self.leaking_ts = now_ts
        if self.left_quata > self.capacity:
            self.left_quata = self.capacity

    def watering(self, quata):
        self.make_sapce()
        if self.left_quata >= quata:
            self.left_quata -= quata
            return True
        return False

funnels = {}

def is_actions_allower(user_id, action_key, capacity, leaking_rate):
    key ='%s:%s'.format(user_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] =funnel
    return funnel.watering(1)

for i in range(20):
    print(is_actions_allower('jason', 'reply', 15, 0.5))

