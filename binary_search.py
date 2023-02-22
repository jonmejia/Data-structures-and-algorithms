# binary searches have to be sorted 
def binary_search(list,target):
    first = 0
    last = len(list) -1
    
    while first <= last:
        midpoint = (first + last)//2
        
        """// is floor division which rounds down to the nearest
        whole number"""
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1
        else:
            last = midpoint -1
    return None

def verify(index):
    if index is not None:
        print(f"target found at index: {index}")
    else:
        print("target not found in list")
        
num_list = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(num_list,2)
verify(result)