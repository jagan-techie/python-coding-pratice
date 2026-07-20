# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

x = "52.625.78467.242.2"
ans = ""
for i in x:
    if i == ".":
        ans += "[.]"
    else:
        ans += i
print(ans)
        
        