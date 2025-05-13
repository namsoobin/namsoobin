M=int(input())
N=int(input())
listO=[int(input()) for i in range(N)]
listR=[j/M*100 for j in listO]
sum1=sum(listR)
최종=sum1/N
print(최종)
