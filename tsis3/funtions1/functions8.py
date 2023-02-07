def spy_game(nums):
    new = [0, 0, 7]
    for i in nums:
        if len(new) == 0:
            return True
        if i == new[0]:
            new.pop(0)
    if len(new) == 0:
            return True
    else:
        return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))