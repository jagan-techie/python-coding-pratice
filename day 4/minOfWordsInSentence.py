# 2114. Maximum Number of Words Found in Sentences
# Example 1:
# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation: 
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.


li = ["hello food a","bad boy","i am pradip"]
ans = 0
for i in li:
    count = 1
    for ch in i:
        if ch == " ":
            count += 1
    ans = max(ans, count)
print(ans)    
    