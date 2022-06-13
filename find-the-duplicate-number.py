# first way
def findDuplicate(nums):
        if len(nums) == 0:
            return 0
        low = 1
        high = len(nums)
        while low < high:
            mid = (low+high)//2
            count = 0
            for x in nums:
                if x <= mid:
                    count = count + 1
            if count > mid:
                high = mid
            else:
                low = mid+1
        return low
print(findDuplicate([1,3,4,2,2]))

# second way
def findDuplicate(nums:list):
    duplicateNum=None
    for i in nums:
        if nums.count(i)>=2:
            duplicateNum = i
    return duplicateNum

print(findDuplicate([3,1,4,2,2]))
