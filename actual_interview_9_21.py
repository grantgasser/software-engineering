"""
Interview Summary

10 minutes of chat, talking about internship
30 minutes of reviewing my find_words solution
    - walking through the code, me explaining
    - correct, but could have been better
    - use collections.deque instead of list (doing inserts or pops from beginning are slow; deque has fast append and pop from both ends)
    - could have constrained location coordinates (maybe with object or algebraic datatype)
        - so that programmer only does (i, j) coordinates and if accidently does (i, i, j) then it throws error
        - taught me about algebraic data types (can say "i AND j" also "in_bounds OR out_of_bounds")
    - BFS starting at each letter repeats work (didn't have time to talk about how to store previous work)
        - maybe a dynamic programming solution? 
    
30 minutes in CoderPad with the below problem
"""

# only for checking
from statistics import median

# Collection of BILLIONS of temps in Fahrenheit, too large to fit in memory, so just keep summary stats 
# too large, can't store all the elements
# temps from -100 to 200

# numbers coming in one at a time
# imagine a Kafka stream coming in...

example = [12, 52, 58, 23, 20, 20, 20, 11, 79, 102, 88, 32, 88, 105, 72, 56, 82]

class Collection(object):
    # me
    def __init__(self):
        self.size = 0
        self.sum = 0
        self.counts = {}

    def append(self, temp):
        self.sum += temp 
        self.size += 1

        # increment
        self.counts[temp] = self.counts.get(temp, 0) + 1

    def seventh(self):
        """
        Don't need to sort the list, just the keys!  
        """
        keys = sorted(list(self.counts.keys()))
        thresh = 7
        total = 0
        for k in keys:
            total += self.counts[k]

            if total >= thresh:
                return k 

    def median(self):
        """
        Didn't get to this in the interview, but this is what we we're leading up to! 

        It's why we needed counts {}. Seventh() was a more straightforward example that we 
        did finish in the interview, but had a little help.
        """
        total = 0
        keys = sorted(list(self.counts.keys()))

        thresh = (self.size // 2) + 1

        for i, k in enumerate(keys):
            total += self.counts[k]

            if total >= thresh:
                if self.size % 2 != 0:
                    return k
                else:
                    return (k + keys[i-1])/2

    def mean(self):
        return self.sum / self.size

    # {-100: 0, 50: 7, 200: 0}, O(|Temps|), in this case just 300, not O(N) where N is size of collection
    def mode(self):
        pass

def main():
    test = Collection()

    example = [12, 52, 58, 23, 20, 20, 20, 11, 79, 102, 88, 32, 88, 105, 72, 56, 82]
    for e in example:
        test.append(e)

    print(test.mean())
    print(test.median() == median(example))
    print(median(example))

main()