#Test1-Anagrams

def mysterious_function(str_a, arg_b, threshold=None):
    ret_val = True
    temp_storage = {}
    temp_storage_2 = {}
    
    if threshold is None:
        threshold = 25
    
    i = 0
    while i < len(str_a):
        c = str_a[i]
        if c != ' ':
            if c.lower() in temp_storage:
                temp_storage[c.lower()] += 1
            else:
                temp_storage[c.lower()] = 1
        i += 1
    

    counter = 0
    for elem in arg_b:
        counter += 1
        if elem == ' ':
            continue
        
        elem = elem.lower()
        if elem in temp_storage_2:
            temp_storage_2[elem] = temp_storage_2[elem] + 1
        else:
            temp_storage_2[elem] = 1
    
  
    for k in temp_storage.keys():
        if k not in temp_storage_2 or temp_storage_2[k] != temp_storage[k]:
            ret_val = False
            break
    
    for k2 in temp_storage_2.keys():
        if k2 not in temp_storage:
            ret_val = False
            break
    
   
    total_chars = sum(temp_storage.values())
    
 
    return ret_val

