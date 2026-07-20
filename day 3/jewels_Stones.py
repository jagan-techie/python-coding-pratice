# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3


stones = "abbbs"
jewels = "ab"
ans = 0
for i in stones:
    if i in jewels:
        ans += 1
print(ans)