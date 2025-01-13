'''
Original Question:
Walls and Gates Problem
You are given an
m x n grid rooms, where:

Each cell can be:
A wall represented by -1
A gate represented by 0
An empty room represented by some large integer (e.g., 2^31 - 1 in the official problem)
You need to fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate (due to walls), leave the distance as is (the large integer).

Example
Input:
[
  [2147483647, -1,           0,           2147483647],
  [2147483647, 2147483647,   2147483647,  -1         ],
  [2147483647, -1,           2147483647,  -1         ],
  [0,          -1,           2147483647,  2147483647]
]

Output:
[
  [3, -1,  0,  1],
  [2,  2,  1, -1],
  [1, -1,  2, -1],
  [0, -1,  3,  4]
]
Here,
A cell with 0 is a gate.
A cell with -1 is a wall, which cannot be passed through.
A cell with a large integer (often 2^31 - 1) is an empty room that needs to be updated with its shortest distance to the nearest gate.
'''

'''
Restate the problem:
Given three states a wall = -1, gate = 0, and empty_room = 2^31, I must replace empty_room cells with the distance from the
nearest gate without crossing a wall. If that is impossible leave the empty_room as is.

CheckList:
- Sources: gates (0)
- Target: empty_rooms (2^31)
- State Changes: empty_rooms get updated with distance to nearest gate
- Parallel wave: potential to have more sources than targets
- Storing time: Store the position of the gates in queue
- Edge cases:
    - if it all walls return as is
    - if there are no gates return as is
- Time complexity: O(m * n)
Ex:
[
  [2147483647, -1,           0,           2147483647],
  [2147483647, 2147483647,   2147483647,  -1         ],
  [2147483647, -1,           2147483647,  -1         ],
  [0,          -1,           2147483647,  2147483647]
]

queue = [(3, 0), (0,2)]
new position = (2, 0)
rooms[new position] = 0 + 1
queue = [(0,2), (2, 0),]
[
  [2147483647, -1,           0,           1          ],
  [2147483647, 2147483647,   1,  -1         ],
  [1,          -1,           2147483647,  -1         ],
  [0,          -1,           2147483647,  2147483647]
]
queue = [(0,2), (2, 0),]
new position = (0, 3)
rooms[new position] = 0 + 1
queue = [(2, 0),(0,3), (1,2)]


[
  [3, -1,           0,           1          ],
  [2,          2,            1,           -1         ],
  [1,          -1,           2,           -1         ],
  [0,          -1,           3,            4]
]
queue = [(0,3), (1,2)]
new position = (1,1)
rooms[new position] = 1 + 1
queue = [(1,2), (1,0), (1,1), (2,2)]



Pseudo:
- Initialize rows
- Initialize cols
- Initialize the queue that stores the gates' positions
- Don't need visited but would need it if we weren't updating the grid
- for loop through the rows and cols,
    if rooms[position] == 0
        - append gates' position to the queue
- if no gates in the queue --> return rooms
- while the queue still has gates
    - for loop through that level (the range(len(queue)))
        - get the gate's position with popleft()
        - initialize all possible moves
        - for loop through the moves and get the new positions
            - check if the new positions are within the constraints of the `rooms` and that the rooms[new position] == 2147483647
                - get rooms[new position] = rooms[old position] + 1
                - append (new position) to the queue
- return rooms
'''

from collections import deque
from typing import List
class Solution:
    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        if not rooms and not rooms[0]:
            return
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        if not len(queue):
            return rooms
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                moves = [(0,1), (1,0), (-1,0), (0, -1)]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and rooms[nx][ny] == 2147483647:
                        rooms[nx][ny] = rooms[x][y] + 1
                        queue.append((nx, ny))
        return rooms


if __name__ == 'main':
    check = Solution()
    example = [[2147483647, 2147483647,  -1,  0], [2147483647, 2147483647, 2147483647, -1],[-1,   2147483647, 2147483647,    2147483647], [0,          -1,         2147483647,    2147483647]]
    result = check.walls_and_gates(example)
    print(result)
