def linear_search(list,target):
    """
    Returns the index position of the target if found, else returns none
    """
    if target in list:
        for i in range(len(list)):
            if list[i] == target:
                return (i)
    else:
        return None

def verify(index):
    if index is not None:
        print(f"target found at index: {index}")
    else:
        print("target not found in list")
        
num_list = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(num_list,6)
verify(result)