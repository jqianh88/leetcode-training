'''
Given two strings `s` and `t`, return true if `t` is an anagram of `s` and false otherwise. 
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
Inputs: 
- s: str
- t: str
Outputs: 
- bool
'''


def valid_anagram(s: str, t: str) -> bool: 
    if len(s) != len(t):
        return False
    s_list = [letter for letter in s]
    t_list = [letter for letter in t]
    for i, s_let in enumerate(s_list):
        if s_let in t_list:
            s_list.pop(i)

    if s_list:
        return True
    return False

if __name__=='__main__':
    s = 'anagram'
    t = 'nagaram'
    print(valid_anagram(s=s, t=t))