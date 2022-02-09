nums=[41,33,17,80,61,5,55,92,4,32, 78]
print(nums)
length = len(nums)
for i in range(length-1):
    for j in range(i+1,0,-1):
        if  nums[j-1] > nums[j]:
            nums[j],nums[j-1] = nums[j-1],nums[j]
print(nums)

