
""" ============================================================================

MATH 352 -- Assignment 2 -- Bonus Question
Matthew Laforce
Created Jan 28, 2025

"Consider a 5×5 grid where each cell is either filled or empty, and all 
configurations are equally likely.

Using a computer to count, find the probability that there is a path (going 
left or right; and up or down, but not diagonally) from the bottom of the grid 
to the top only going through filled cells."

Grid Representation:
    25  24  23  22  21
    20  19  18  17  16
    15  14  13  12  11
    10  09  08  07  06
    05  04  03  02  01
Where filled-in cells are represented using a '1', and where empty cells are 
represented using '0'. Then, the binary value 0b1000010000100001000010000 is
a grid with only the rightmost column filled, and nothing else.

============================================================================ """

# Hardcoded values for 'quickcheck' method (below)
cols = [0b1000010000100001000010000,
        0b0100001000010000100001000,
        0b0010000100001000010000100,
        0b0001000010000100001000010,
        0b0000100001000010000100001]
rows = [0b1111100000000000000000000,
        0b0000011111000000000000000,
        0b0000000000111110000000000,
        0b0000000000000001111100000,
        0b0000000000000000000011111]

def quickcheck(grid):
    """
    Accepts 'grid', a binary number having length 25, where the values
    represent filled-in cells. 
    
    Performs a preliminary, relatively fast check of 'grid' looking for two 
    common patterns:
    - If a complete column is found, returns '1' representing a valid path;
    - If an empty row is found, returns '0' indicating no path can exist;
    
    Else, quickcheck returns a value of '-1', which tells it's caller to run 
    the more thorough 'deepcheck' method.
    """
    for val in cols:
        if (val & grid) == val:
            return 1
    for val in rows:
        if (val & grid) == val:
            return (0)
    return -1

def deepcheck(grid):
    """
    Accepts 'grid', a binary number having length 25, where the values
    represent filled-in cells. 
    
    Performs a thorough search to determine whether any viable path exists
    through the given grid. Returns a value of '1' if a path exists, else
    returns a value of '0'.
    """
    stack = []
    # Convert the binary value into a list of cells 'unvisited'
    unvisited = []
    str_grid = str(grid)
    counter = 1
    for bit in str_grid[:1:-1]:     # Add to 'unvisited' smallest to largest
        if int(bit) == 1:
            unvisited.append(counter)
        counter += 1
    # Push all bottom-row values onto the stack (values 5 or less)
    for item in range(1,6):
        if item in unvisited:
            stack.append(item)
    # While the stack is non-empty, pop and search for new values
    while (len(stack) > 0):
        cur_cell = stack.pop()
        # If cur_cell reaches the top row (21-25), return '1'
        if (cur_cell >= 21):
            return 1
        # Otherwise, check for adjacencies relative to cur_cell
        if (cur_cell - 5) in unvisited:
            # Downwards check: adjacencies removed from 'unvisited', added to stack
            down_position = unvisited.index(cur_cell - 5)
            down_cell = unvisited.pop(down_position)
            stack.append(down_cell)
        if (cur_cell + 1) in unvisited and (cur_cell % 5 != 0):
            # Leftwards check
            left_position = unvisited.index(cur_cell + 1)
            left_cell = unvisited.pop(left_position)
            stack.append(left_cell)
        if (cur_cell - 1) in unvisited and (cur_cell % 5 != 1):
            # Rightwards check
            right_position = unvisited.index(cur_cell - 1)
            right_cell = unvisited.pop(right_position)
            stack.append(right_cell)
        if (cur_cell + 5) in unvisited:
            # Upwards check: perform this check last to maximize it's priority
            up_position = unvisited.index(cur_cell + 5)
            up_cell = unvisited.pop(up_position)
            stack.append(up_cell)
    return 0
    
def grid_counter():
    """
    Main method for this question. Uses the helper methods above to determine
    whether individual grids are valid or not.
    
    The grid itself is represented using a 25-digit binary value, with the '1s'
    position corresponding with the bottom-right corner, and with the '25s' 
    position representing the top-left corner.
    
    The grid would begin as 'empty', except no possible valid grid can appear
    until all rows are populated: starting from "0b0000100001000010000100001"
    still ensures no missed values, and saves 1082402 pointless applications of 
    'quickcheck'.
    """
    count = 0
    grid = 0b0000100001000010000100001
    while (grid <= 0b1111111111111111111111111):
        # Print the progress the program is making
        if grid % 1000 == 0:
            print(f"Processing grid {grid}/{2**25}")            
        validate_grid = quickcheck(grid)
        if (validate_grid == (-1)):
            validate_grid = deepcheck(grid)
        count += validate_grid
        grid += 1
    print(f"\nValid grids counted: {count}")
    input("Press 'Enter' to exit.")

if __name__ == '__main__':
    grid_counter()
