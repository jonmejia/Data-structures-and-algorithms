def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        
        if list[midpoint] == target:
            return True

    