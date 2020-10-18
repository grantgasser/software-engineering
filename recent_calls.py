class RecentCounter:

    def __init__(self):
        self.q = []

    def ping(self, t: int) -> int:
        s = t - 3000
        self.q.append(t)
        
        while self.q[0] < s:
            self.q.pop(0)
        
        return len(self.q)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)