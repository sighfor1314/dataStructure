import random

'''
bubble Sort n^2
'''
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1-i):
#         if nums[j+1]<nums[j]:
#             nums[j],nums[j+1]=nums[j+1],nums[j]
#
# print(nums)
'''
selection Sort n^2
'''
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] > nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
# print(nums)

# for i in range(len(nums)-1):
#     for j in range(i+1,0,-1):
#         if nums[j-1]> nums[j]:
#             nums[j], nums[j - 1] = nums[j - 1], nums[j]
#
# print(nums)

def quick_sort(nums):
    if len(nums) <=1:
        return nums
    left= []
    right=[]
    piv=[]
    a=nums[0]
    for i in nums:
        if a < i:
            right.append(i)
        elif a> i :
            left.append(i)
        else:
            piv.append(i)
    return (quick_sort(left)+piv+quick_sort(right))


nums=[]
for i in range(10):
    nums.append(random.randint(0,1000))

print('origin=',nums)
print(quick_sort(nums))
