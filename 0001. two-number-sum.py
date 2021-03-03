'''
o(n^2) time | o(1) space
def twoSum(array,target):
    l=len(array)
    for i in range(l-1):
        num1=array[i]
        for j in range(i+1,l):
            num2=array[j]
            if num1+num2==target:
                return [num1,num2]
    return []
array=[2,3,11,1,-1,15]
target=10
print(twoSum(array,target))



o(n) time | o(n) space
def twoSum(array,target):
    nums={}
    for num in array:
        temp=target-num
        if temp in nums:
            return [temp,num]
        else:
            nums[num]=True
    return []
array=[2,3,11,1,-1,15]
target=10
print(twoSum(array,target))



o(n logn) time | o(1) space
def twoSum(array,target):
    array.sort()
    left=0
    right=len(array)-1
    while left<right:
        if array[left]+array[right]==target:
            return [array[left],array[right]]
        elif array[left]+array[right]>target:
            right=right-1
        elif array[left]+array[right]<target :
            left=left+1
    return []
array=[2,3,11,1,-1,15]
target=10
print(twoSum(array,target))
'''

