'''
palindrome = 회문. 앞 뒤가 똑같은 단어나 문장.
'''
text = "A man, a plan, a canal: Panama"
words = ''.join(c for c in text if c.isalnum()).lower()
for i in range (len(words)//2):
    if words[i] != words[-(i+1)]: 
        print(False)
        break
else: print(True)