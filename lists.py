''''list=[1,2,3,4,5]
print(len(list))'''

#slicing
''''marks=[20,30,45,65,32,100.0]
print(marks[2:5])
print(marks[-5:-2])  #negative indexing
marks.append(90)
print(marks)'''

#loops
''''nums=[1,2,3,4,5]
x=3
indx=0
for val in nums:
    if val==x:
        print(f"{x} found at index = {indx}")
        break
    indx+=1'''

nums=[1,2,3,4,5,2,1]
nums.sort()
print(nums)
