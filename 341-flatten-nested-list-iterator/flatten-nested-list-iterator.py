# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from types import  GeneratorType
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def flatten_next(res):
            # loop throuh each elements
            for sub_list in res:
                # if curr element is list, then call flatten_next
                tmp_list = sub_list.getList()
                tmp_val = sub_list.getInteger()
                if tmp_list:
                    yield from flatten_next(tmp_list)
                # if curr is not list , then return value
                if sub_list.isInteger():
                    yield tmp_val
    
        # init generator
        self.list_genrator = flatten_next(nestedList)
        
        # next values
        self.next_val = next(self.list_genrator,None)
    


    def next(self) -> int:
        result = self.next_val
        self.next_val = next(self.list_genrator,None)
        # return 
        return result
        

    def hasNext(self) -> bool:
        return self.next_val is not None


         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())