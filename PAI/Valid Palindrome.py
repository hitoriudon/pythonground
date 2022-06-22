'''
palindrome = 회문. 앞 뒤가 똑같은 단어나 문장.
'''
import collections


text = "A man, a plan, a canal: Panama"

def my_sol(): #304ms for executing
    words = ''.join(c for c in text if c.isalnum()).lower()
    for i in range (len(words)//2):
        if words[i] != words[-(i+1)]: 
            return False
    return True

def deque_sol(): #64ms for executing
    strs = collections.deque()
    for char in text:
        if char.isalnum():
            strs.append(char.lower())        
    while len(strs)>1:
        if strs.popleft() != strs.pop(): #popleft() time complexity is O(1)
            return False
    return True

print(deque_sol())
print(my_sol())