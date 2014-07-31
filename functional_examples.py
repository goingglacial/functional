#implementation of map function

def annie_map(f,lst):
    '''
    For function and list, apply function
    to all elements of the list, return
    function(list).
    '''
    result = []
    for i in lst:
        result.append(f(i))
    return result

#implementation of reduce function

def annie_reduce(f, seq):
    '''
    Return one value by combining
    elements in a list according
    to a specific function.
    '''
    #get 'leftmost' value in seq
    total = seq[0]
    #for all other values in seq
    for i in seq[1:]:
        total = f(total, i)
    return total
