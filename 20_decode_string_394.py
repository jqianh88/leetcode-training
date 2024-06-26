class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_str = ""
        k = 0

        for char in s:
            if char.isdigit():
                # Build the number k (could be more than one digit)
                k = k * 10 + int(char)
            elif char == '[':
                # Push the current k and current_str onto the stacks
                num_stack.append(k)
                str_stack.append(current_str)
                # Reset current_str and k
                current_str = ""
                k = 0
            elif char == ']':
                # Pop the last k and last_str from the stacks
                last_k = num_stack.pop()
                last_str = str_stack.pop()
                # Repeat current_str last_k times and concatenate with last_str
                current_str = last_str + last_k * current_str
            else:
                # Build the current string
                current_str += char

        return current_str


