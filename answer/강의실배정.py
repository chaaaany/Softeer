import sys
import heapq

n = int(sys.stdin.readline())

#시간복잡도 감소를 위해 heap 사용하기
heap = []
for a in range(n) : 
    s, f = map(int, sys.stdin.readline().split())
    #f를 기준으로 (f, s) 가 heap에 저장된다.
    heapq.heappush(heap, (f, s))

#초깃값
temp = 0
count = 0
#heap리스트가 0일때 까지 반복한다.
while heap :
    f, s = heapq.heappop(heap)
    #앞의 끝나는 시간 < 뒤의 시작 시간
    if(temp <= s) :
        count += 1
        temp = f
print(count)