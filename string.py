import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
# changing first element  
   
add=int(input("enter your age :") )  # Output: array('i', [0, 2, 3, 5, 7, 10])  
numbers[0] = (add)

# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # Output: array('i', [0, 2, 4, 6, 8, 10])