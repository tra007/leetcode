listsum=[]
def twoSum(nums:list, target):
    for index,i in enumerate(nums):
        for b in nums[index+1:]:
            if (i+b==target):
                num1=index
                num2=nums.index(b)
                if (num1==num2):
                    num2+=1
                listsum.extend([num1,num2])
                return listsum
lists=[3,3]
target=6

print(twoSum(lists,target))

