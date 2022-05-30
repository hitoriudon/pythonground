import time
import requests
import multiprocessing #threading을 쓸 줄 모르고, 새로 배우기 귀찮아서... 그냥... 이걸로 했음
def func(): #target function
    current = multiprocessing.current_process() #method
    thread_id = int(current.name[8]) #get the value of thread_id (1,2,3)
    for day in range (1, 16): #day1~ day15
        try:
            #method. Using api_key of NASA
            url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=201%i-6-%i&api_key=Xzfc5c6PLV7m9XZwQxV6g7UvApNnSVZvfc3GKWxJ" %(thread_id+4, day)
            response = requests.get(url).json() #method
            time.sleep(1)
            print(response['photos'][0]['img_src'], end=" ")
            print(response['photos'][0]['earth_date'], end=" ")
            print("Thread-%i" %(thread_id))
        except IndexError: #IndexError일때만 여기로 빠지는 예외처리.
            print("201%i-6-%i의 데이터가 비어있습니다." %(thread_id+4, day))
            '''
            2017년 6월 1일에서 IndexError가 발생하고, 그 결과 Thread-3이 실행이 되지 않았습니다.
            2017년 6월 1일의 response 딕셔너리를 확인해본 결과, {'photos': []}가 출력되었습니다.
            key값은 있으나 value값이 비어있어 img_src와 earth_date의 값을 얻을 수 없기에,
            데이터가 비어있음을 알려주는 exception 처리를 했습니다.
            '''
if __name__ == '__main__':
    for _ in range (3):
        threads = multiprocessing.Process(target=func) #method
        threads.start() #method