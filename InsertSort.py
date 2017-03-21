# -*- coding:utf-8 -*-
# 插入排序
Data = [5,3,3,4,6,2,4,6]
Sorted_Data = []
Sorted_Data.append(Data[0])


if Data[1] <= Sorted_Data[0]:
    Sorted_Data.insert(0,Data[1])
else:
    Sorted_Data.append(Data[1])

for i in Data[2:]:
    if i < Sorted_Data[0]:
        Sorted_Data.insert(0,i)
    elif i > Sorted_Data[len(Sorted_Data)-1]:
        Sorted_Data.append(i)
    else:
        for j in range(0,len(Sorted_Data)-1):
            if i >= Sorted_Data[j] and i <= Sorted_Data[j+1]:
                Sorted_Data.insert(j+1,i)

print Sorted_Data


