class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):

        # creating  combination generators
        def combinations(iterable, r):
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))

            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    print(indices[i] , i + n - r)
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1] + 1
                yield tuple(pool[i] for i in indices)

        # intialzie the variables
        self.chars_comb_gen = combinations(characters, combinationLength)
        tmp_val =  next(self.chars_comb_gen,None)
        if tmp_val:
            self.next_val = ''.join(tmp_val)
        else:
            self.next_val = None

    def next(self) -> str:
        result = self.next_val
        tmp_val =  next(self.chars_comb_gen,None)
        if tmp_val:
            self.next_val = ''.join(tmp_val)
        else:
            self.next_val = None
        # return 
        return result


    def hasNext(self) -> bool:
        return self.next_val is not  None