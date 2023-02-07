def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
        
#num = [1, 3, 3]
#num = [1, 3, 1, 3]
num = [3, 1, 3]
print(has_33(num))