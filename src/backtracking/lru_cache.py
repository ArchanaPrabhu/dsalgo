class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.q = deque()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("get", key ,self.cache, self.q)
        if key in self.cache:
            if (key in self.q):
                self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print("put", key, value, self.cache, self.q)
        if (key in self.cache):
            self.cache[key] = value
            
        elif (len(self.q) == self.capacity):
            v = self.q.popleft()
            if v in self.cache:
                del self.cache[v]


        self.cache[key] = value
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
