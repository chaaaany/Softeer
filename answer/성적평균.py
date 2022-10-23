import sys
import math
n, k = map(int, input().split())
score = list(map(int, input().split()))

mylist=[list(map(int, input().split())) for _ in range(k)]

answer = []
start = 0
finish = 0
for num in range(k) : 
    start = mylist[num][0]-1
    finish = mylist[num][1]
    answer.append(round((sum(score[start:finish])/(finish-start)),2))
for ans in answer : 
    print(format(ans, ".2f"))