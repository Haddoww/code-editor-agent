
def find_extreme_values_convoluted(input_array):

    if not input_array:
        return None, None
    
  
    working_array = []
    for i in range(len(input_array)):
        working_array.append(input_array[i])
    
    current_min_value = None
    current_max_value = None
    min_index = -1
    max_index = -1
    
    initialized = False
    

    for idx, item in enumerate(working_array):
 
        if item is None:
            continue
            
       
        if not initialized:
            current_min_value = item
            current_max_value = item
            min_index = idx
            max_index = idx
            initialized = True
            continue
        
       
        if item < current_min_value:
            temp_min = item
            current_min_value = temp_min
            min_index = idx
        
       
        if item > current_max_value:

            temp_max = item
            current_max_value = temp_max
            max_index = idx
    
  
    for i in range(0, len(working_array)):
        element = working_array[i]
        
      
        if element is None:
            continue
            
      
        if element < current_min_value:

            current_min_value = element
            min_index = i
        
      
        if element > current_max_value:
            current_max_value = element
            max_index = i
    
    
    value_counts = {}
    
   
    for value in working_array:
        if value is not None:
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
    
   
    min_count = 0
    if current_min_value in value_counts:
        min_count = value_counts[current_min_value]
    
   
    max_count = 0  
    if current_max_value in value_counts:
        max_count = value_counts[current_max_value]
    
   
    min_result = {
        'value': current_min_value,
        'index': min_index,
        'occurrences': min_count
    }
    
    max_result = {
        'value': current_max_value,
        'index': max_index,
        'occurrences': max_count
    }
    
    
    final_min = min_result['value']
    final_max = max_result['value']
   
    sorted_array = sorted(working_array, key=lambda x: float('-inf') if x is None else x)
    sorted_array = [x for x in sorted_array if x is not None]
    
    if sorted_array:
    
        if sorted_array[0] != final_min:
          
            final_min = sorted_array[0]
            
        if sorted_array[-1] != final_max:
          
            final_max = sorted_array[-1]
    
  
    return final_min, final_max
