# ANSI escape codes for some colors
RED_AOCTOOLS = '\033[91m'
GREEN_AOCTOOLS = '\033[92m'
YELLOW_AOCTOOLS = '\033[93m'
BLUE_AOCTOOLS = '\033[94m'
MAGENTA_AOCTOOLS = '\033[95m'
CYAN_AOCTOOLS = '\033[96m'
WHITE_AOCTOOLS = '\033[97m'
RESET_AOCTOOLS = '\033[0m'  # Resets the color to default

"""
# Example usage
print(RED + "This is red text." + RESET)
print(GREEN + "This is green text." + RESET)
print(YELLOW + "This is yellow text." + RESET)
"""

def print_2darrays_side_by_side(array1, array2,array1_sub_array3=None):
    """ Takes 2 arrays and displays them. It's good for spacing"""
    # Find the maximum width of any number in array2 for proper spacing
    
    if array1_sub_array3 == None:
        max_width = max(
                len(str(element))
                for array in (array1, array2)
                for row in array
                for element in row)
    #If you make somewhere non character affecting changes, such as using ANSI colors, you need to have flag be True
    else:
        max_width = max(
                len(str(element))
                for array in (array1_sub_array3, array2)
                for row in array
                for element in row)
        

    # Determine the number of rows and columns
    num_rows = len(array1)
    num_columns = len(array1[0])

    # Print column indices
    print("".join(f"_"*len(str(num_rows))), "_".join(f"{i:>{max_width}}" for _ in range(2) for i in range(num_columns)))

    # Print each row with row indices
    for i in range(num_rows):
        # Print row index for array 1
        print(f'{i:{len(str(num_rows))}}:',end="")
        # Print array1 elements
        for element in array1[i]:
            print(f"{element:>{max_width}}", end=" ")
        for element in array2[i]:
            print(f"{element:>{max_width}}", end=" ")
        print()

"""array1 = [['a', 'b', 'c'], ['d', 'e', 'f']]
array2 = [[123, 45, 6], [78900000, 12, 345]]

print_2darrays_side_by_side(array1, array2)"""

