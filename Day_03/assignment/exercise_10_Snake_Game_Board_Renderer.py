"""
Exercise 10: Snake Game Board Renderer

Render a simple 2D text game board.
Steps:
1. Create a 5x5 grid filled with dots "."
2. Place food "F" at position [2, 3]
3. Prompt user for snake head coordinates [row, col]
4. Place snake head "S" at user coordinates
5. If coordinates are [2, 3], print "Yum! The snake ate the food!"
6. Print the grid neatly (elements separated by spaces)
"""

# Create a 5x5 grid filled with dots
grid = [["." for _ in range(5)] for _ in range(5)]

# Place food at position [2, 3]
grid[2][3] = "F"

# Prompt for snake coordinates
row = int(input("Enter snake head row (0-4): "))
col = int(input("Enter snake head column (0-4): "))

# Place snake head at the given position
grid[row][col] = "S"

# Print the grid
for row_list in grid:
    print(" ".join(row_list))

# Check if snake ate the food
if row == 2 and col == 3:
    print("Yum! The snake ate the food!")
