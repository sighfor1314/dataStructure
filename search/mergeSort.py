def merge(left,right):
    result =[]
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result+=left
    if right:
        result+=right
    return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid= len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left,right)
data = [6, 1, 5, 7, 3, 9, 4]
print("原是串列：", data)
print("排序結果：", merge_sort(data))