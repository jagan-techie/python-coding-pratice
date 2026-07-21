# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


nums = [2,7,11,15]
target = 18
for i in range(len(nums)):
    a = nums[i]
    b = nums[i+1]
    if target == a + b:
        break
print(i,i+1)
    