import hashlib
import pandas as pd

if __name__=='__main__':
    binsum=''
    x=-1
    nonceList = []
    for i in range (1,21):
        while True:
            string = 'homework'+str(x) 
            encoded_string = string.encode()
            hexdigest = hashlib.sha256(encoded_string).hexdigest() # H('homework'||nonce)
            encoded_hexdigest = hexdigest.encode()
            hexdigest = hashlib.sha256(encoded_hexdigest).hexdigest() # H( H('homework'||nonce) )
            binsum=''
            x+=1
            for k in range (5):
                if 48<=ord(hexdigest[k])<=57:
                    n = int(hexdigest[k])
                else: 
                    n = ord(hexdigest[k])-55
                mod = 0
                slist = ''
                for j in range (4):
                    mod = n%2
                    if n==0:
                        slist += '0'
                    else:
                        slist += str(mod)
                    n = n // 2
                tmp = slist[::-1]
                binsum+=tmp
            if binsum[0:i] == '0'*i:
                nonceList.append(x)
                x=-1
                break
    series = pd.Series(nonceList)
    print(series.plot())

''' <<<의식의 흐름 주의>>>
encode하고 sha256적용해서 hexdigest()하게 되면 64개의 16진수가 출력됩니다.
과제는 0, 00, 000, 0000... 가 나오는 이진수 nonce의 값을 찾는 것이기 때문에
hexdigest값을 2진수로 바꿔주는 작업이 필요할 것입니다.
bin()으로 할 수 없는데, 7은 이진수로 0111인데 bin(7)을 하게 되면 111만 출력됩니다. 앞에 있는 0은 자동으로 생략된다는 뜻이죠? 
그래서 우린 16진수를 2진수로 바꿀 때 네 칸을 그대로 유지하기 위해 이진수 전환하는 코드를 직접 구현해야 합니다. 
근데 64비트 16진수를 다 바꿔주면 총 256비트가 되는데... 다 바꿔줄 필요가 있을까요?
0부터 20비트까지만 0인지 nonce를 확인하는 게 과제니까 16진수 64개로 이루어진 hexdigest의 0,1,2,3,4번째까지만 2진수로 바꿔주면 
2진수 20비트가 될 것입니다. 그 값은 binsum에 저장할 것입니다. for k에서 숫자일 경우와 알파벳일 경우를 아스키 코드를 활용해 구분했습니다. 
이제 0번째 hexdigest를 십진수로 바꿔주었으니 이진수로 바꿔줘야겠죠? 
for j에서 if, else로 분기했습니다. 몫이 0이면 0을 slist에 채워넣고 아니면 나머지를 채워넣었습니다. (7 -> 1110)인 상태입니다. 0111이 되기 위해 뒤집어줘야합니다.
slist를 뒤집어 준 값을 tmp에 저장하고 binsum에 추가해줬습니다.
이제 마지막으로 nonce 값인 변수 x가 0, 00, 000, 0000의 nonce인지 비교해주는 if binsum[0:i]== '0'*i 코드를 추가합니다. 찾으면, x를 다시 -1로 초기화합니다.
if 조건문이 참이 아니라면 다시 무한루프 수행하러 가고.. 계속 x+=1하면서 찾겠죠 뭐..
교수님이 plot 하라고 하셔서 pandas 라이브러리 활용해서 series 타입으로 저장해서 plot() 썼습니당
'''
# 여기서 궁금증. x=-1로 초기화를 다시 해줘야 하는가? (결과 속도에 엄청난 차이)