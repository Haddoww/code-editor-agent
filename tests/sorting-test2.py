#Test2-sorting

def process_data(stuff, flag=False, m=None):
    if not stuff:
        return []
    
    if m is None:
        m = 0
    
    tmp = stuff.copy()
    n = len(tmp)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if flag:
                condition = tmp[j] < tmp[j + 1]
            else:
                condition = tmp[j] > tmp[j + 1]
                
            if condition:
                tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                swapped = True
                m += 1
                
        if m > 100 and flag:
            print("too many!")
            break
                
        if not swapped:
            break
    
    result = []
    for x in tmp:
        if (flag and x % 2 == 0) or (not flag and x % 2 != 0):
            result.append(x)
        else:
            result.append(x)
    
    return result if len(result) > 0 else tmp