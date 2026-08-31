"""
Exercise 7: Treasure Map Coordinate Filter

You have a list of coordinate pairs representing suspected treasure locations.
Treasure can ONLY exist in the first quadrant where x > 0 AND y > 0.

HINTS:
- coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
- Use list comprehension: [[x, y] for x, y in coords if condition]
- Condition: check if both x > 0 AND y > 0
- Print filtered valid coordinates

Expected output: [[12, 5], [15, 9]]
"""

# TODO: Initialize coords list (hardcoded)
# TODO: Create list comprehension to filter coordinates
# TODO: Condition: x > 0 and y > 0
# TODO: Print valid coordinates
def main():

    # coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    # ns = [[x,y] for x,y in coords if x>0 and y>0] 
    # print(ns)
    
    x = int(input("Enter the number of coordinates:"))
    nested_list = []

    for i in range(x):
        row = list(map(int, input().split()))
        if row[i]>0:
            nested_list.append(row)
    selected_coords =  [[x,y] for x,y in nested_list if x>0 and y>0]
    print(selected_coords)
       
if __name__=="__main__":
    main()