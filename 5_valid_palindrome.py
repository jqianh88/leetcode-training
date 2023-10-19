"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers. 
Given a string s, return true if it is a palindrome, or false otherwise. 

Inputs: 
- s: string

Outputs: 
- palindrome: bool
"""

def palindrome(s: str) -> bool:
    palindrome = []
    for letter in s: 
        if letter.lower().isalnum():
            palindrome.append(letter.lower())
    new_string = "".join(palindrome)
    reverse_new_string = new_string[::-1]
    half_len = len(new_string)//2
    first_half = new_string[:half_len]
    second_half = reverse_new_string[:half_len]
    if not first_half == second_half:
        return False
    return True 
    

if __name__=='__main__':
    s = ' ' #'A man, a plan, a canal: Panama'  # 'race a car' " "
    print(palindrome(s=s))