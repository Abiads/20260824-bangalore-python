"""
Exercise 9: The Josephus Elimination Game

A group of N soldiers (numbered 1 to N) stand in a circle.
Every K-th soldier is eliminated from the circle, count continues circularly.

HINTS:
- Get N (number of soldiers) and K (elimination interval) from user
- Create soldier_circle = list(range(1, N + 1))
- Use a loop: while len(soldier_circle) > 1:
- Track current_index in the circle
- Use modulo (%) operator to wrap around: current_index = (current_index + K - 1) % len(soldier_circle)
- Use list.pop(current_index) to remove and get eliminated soldier
- Adjust index after each removal
- Print each elimination step
- Print final survivor

Example: N=5, K=2 → Eliminate 2, 4, 1, 5 → Survivor: 3
"""

# TODO: Get N and K from user
# TODO: Initialize soldier circle with numbers 1 to N
# TODO: Set current_index = 0
# TODO: While more than 1 soldier remains:
  # TODO: Calculate next elimination index using modulo
  # TODO: Remove soldier at that index
  # TODO: Print eliminated soldier and remaining soldiers
# TODO: Print final survivor
