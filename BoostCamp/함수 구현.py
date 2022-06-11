def solution (arr):
    elements = list(set(arr))
    result = []
    for i in elements: 
        if arr.count(i)>=2 : result.append(arr.count(i))
    return [-1] if len(result)==0 else result
arr = [1,3,5,7,9]
#arr = [3, 2, 4, 4, 2, 5, 2, 5, 5]
#arr = [1, 2, 3, 3, 3, 3, 4, 4]
print(solution(arr))
