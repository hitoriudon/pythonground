k = int(input())
temp = [int(2+(n**2+n)/2) for n in range (k-1)]
answer = [1]
for i in range(k-1):
    answer.append(1+sum(temp[:i+1]))
print(answer[k-1]) #k-1 index

'''
15분 썼음ㅋㅋㅋ하아
'''
