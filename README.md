#정수 무작위로 N개 출력
import random
N=random.randint(0, 1000000)
#리스트에 N번을 반복해서 랜덤한 정수를 입력하고 싶은데 random함수에 대해 잘 모르겠음...
for list1 in range(N):
  int1=random.randint(-10000000,1000000)
  list1.append(int1)
#sorted() 써서 오름차순으로 정렬
list2 = sorted(list1)
print(list2)
#오름차순으로 정렬한 리스트에 처음 값(최댓값), 마지막 값(최솟값) 출력
print(list2[0],list2[-1])
