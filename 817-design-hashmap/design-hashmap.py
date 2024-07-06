from collections import defaultdict as df
class MyHashMap:

    def __init__(self):
        # init dautl dict with defautl value -1
        self.key_map = df(lambda :-1)
        

    def put(self, key: int, value: int) -> None:
        # update/insert new value for the key
        self.key_map[key] = value

    def get(self, key: int) -> int:
        # return value else -1
        return self.key_map[key]
        

    def remove(self, key: int) -> None:
        # pop the key
        self.key_map.pop(key) if self.key_map[key] !=-1 else None

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)