from array import *
arr1=array('i',[4,9,5])
arr2=array('i',[9,4,9,4,8])
arr3=array('i',[])
for i in range(0, len(arr1)):
    for j in range(0,len(arr2)):
        if arr1[i]==arr2[j]:
            arr3.append(arr1[i])

arr3=list(set(arr3))

print(arr3)



