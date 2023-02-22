def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:])
            else:
                return recursive_binary_search(list[midpoint+1:])

def verify(result):
    print(f"Target found: {result}")

num_list = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(num_list,6)
verify(result)



    