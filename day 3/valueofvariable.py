# Input: operations = ["--X","X++","X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X =  0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 =  0.
# X++: X is incremented by 1, X =  0 + 1 =  1.

operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i == "--X" or i == "X--":
        x -= 1
    else:
        x += 1
print(x)
        
        
        