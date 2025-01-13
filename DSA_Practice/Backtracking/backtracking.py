'''
Backtracking
Definition: Backtracking is an algorithmic technique that builds candidates for solutions incrementally and abandons a candidate ("backtracks") as soon as it determines the candidate cannot lead to a valid solution.
Key Components:
- State Space: The potential solutions you are exploring.
- Recursive Call: How the algorithm moves deeper into the state space.
- Pruning: Exclude paths early that cannot yield valid solutions.
- Base Case: When a valid solution is found or all candidates have been explored.

Use Cases: permutations, combinations, subset generation, N-Queens, Sudoku Solver
'''
### General Backtracking Framework
def backtrack(state, options):
    # Base case: Check if the current state is a solution
    if is_solution(state):
        process_solution(state)
        return

    for option in options:
        if is_valid(option, state):  # Prune invalid candidates
            state.add(option)  # Make a move
            backtrack(state, options)  # Recurse
            state.remove(option)  # Undo the move


