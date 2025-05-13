list1=[int(input()) for i in range(10)]
list2=[j%42 for j in list1]
list3=set(list2)
length=len(list3)
print(length)
