from collections import defaultdict;


def makeAHashTableForStringCharandTherCount(strs):
    counter = defaultdict(int) #key is char : val is count of char
    for i in strs:
        counter[i] = 1 + counter.get(i,0)
            
            
    print(counter)
    # print(counter.sort())
    
    print(counter)
    
    #  {'a': 5, 'b': 5, 'c': 3, 'f': 1, 'd': 1})
    
    


string = "abcbabababacfdc"
print(len(string))
makeAHashTableForStringCharandTherCount(string)

    