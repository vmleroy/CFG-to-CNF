def convertListToStr(s):
    # initialization of string to ""
    new = ""
    # traverse in the string 
    for x in s:
        new += x 
    # return string 
    return new

def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]
