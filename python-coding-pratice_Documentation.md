### 📄 d:\Vs Code\python-coding-pratice\additional.py
*Saved at: 7/16/2026, 8:05:56 AM*

**[REMOVED]**
```
(from line ~4)
    # Counter automatically adds values for matching keys

```

---

### 📄 d:\Vs Code\python-coding-pratice\additional.py
*Saved at: 7/16/2026, 8:05:52 AM*

**[ADDED]**
```
1     from collections import Counter
2     
3     def merge_inventories(dict1, dict2):
4         # Counter automatically adds values for matching keys
5         return dict(Counter(dict1) + Counter(dict2))
6     
7     store_a = {'apples': 10, 'bananas': 5, 'oranges': 8}
8     store_b = {'bananas': 12, 'oranges': 2, 'grapes': 15}
9     
10    combined = merge_inventories(store_a, store_b)
11    print("Merged Inventory:", combined)
```

---

### 📄 d:\Vs Code\python-coding-pratice\list\list1.py
*Saved at: 7/15/2026, 9:25:28 AM*

**[REMOVED]**
```
(from line ~11)
    # Condition 1: Print if divisible by 5

```

---

### 📄 d:\Vs Code\python-coding-pratice\list\list1.py
*Saved at: 7/15/2026, 9:25:24 AM*

**[REMOVED]**
```
(from line ~4)
    # Condition 3: Stop the loop if number > 500

```
**[ADDED]**
```
4     
```

---

### 📄 d:\Vs Code\python-coding-pratice\list\list1.py
*Saved at: 7/15/2026, 9:25:20 AM*

**[REMOVED]**
```
(from line ~8)
    # Condition 2: Skip the number if > 150

```

---

### 📄 d:\Vs Code\python-coding-pratice\list\list1.py
*Saved at: 7/15/2026, 9:25:16 AM*

**[ADDED]**
```
1     numbers = [12, 75, 150, 180, 145, 525, 50]
2     
3     for item in numbers:
4         # Condition 3: Stop the loop if number > 500
5         if item > 500:
6             break
7         
8         # Condition 2: Skip the number if > 150
9         if item > 150:
10            continue
11        
12        # Condition 1: Print if divisible by 5
13        if item % 5 == 0:
14            print(item)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/15/2026, 9:17:04 AM*

**[REMOVED]**
```
(from line ~11)
        print(item)push
```
**[ADDED]**
```
11            print(item)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:43 PM*

**[REMOVED]**
```
(from line ~7)


```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:40 PM*

**[REMOVED]**
```
(from line ~11)
  

```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:37 PM*

**[REMOVED]**
```
(from line ~4)
    # Condition 3: Stop the loop if number > 500

```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:31 PM*

**[REMOVED]**
```
(from line ~8)
    # Condition 2: Skip the number if > 150

```
**[ADDED]**
```
8     
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:28 PM*

**[REMOVED]**
```
(from line ~12)
    # Condition 1: Print if divisible by 5

```
**[ADDED]**
```
12      
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop3.py
*Saved at: 7/14/2026, 11:55:23 PM*

**[ADDED]**
```
1     numbers = [12, 75, 150, 180, 145, 525, 50]
2     
3     for item in numbers:
4         # Condition 3: Stop the loop if number > 500
5         if item > 500:
6             break
7         
8         # Condition 2: Skip the number if > 150
9         if item > 150:
10            continue
11        
12        # Condition 1: Print if divisible by 5
13        if item % 5 == 0:
14            print(item)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:52:57 PM*

**[REMOVED]**
```
(from line ~10)
print(f"the current number is: {i} and the cube is {i**3}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i**3}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:52:34 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i**3}")
```
**[ADDED]**
```
10    print(f"the current number is: {i} and the cube is {i**3}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:52:20 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i***3}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i**3}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:52:08 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i*}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i***3}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:52:06 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i*i*i}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i*}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:38 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i*i**}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i*i*i}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:35 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i*i}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i*i**}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:33 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {i}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i*i}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:31 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {i} and the cube is {}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {i}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:18 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {} and the cube is {}")
```
**[ADDED]**
```
10        print(f"the current number is: {i} and the cube is {}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:08 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {} and the cub")
```
**[ADDED]**
```
10        print(f"the current number is: {} and the cube is {}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:51:04 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: {}")
```
**[ADDED]**
```
10        print(f"the current number is: {} and the cub")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:59 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: ")
```
**[ADDED]**
```
10        print(f"the current number is: {}")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:57 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: "")
```
**[ADDED]**
```
10        print(f"the current number is: ")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:55 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is: ")
```
**[ADDED]**
```
10        print(f"the current number is: "")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:53 PM*

**[REMOVED]**
```
(from line ~10)
    print(f"the current number is")
```
**[ADDED]**
```
10        print(f"the current number is: ")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:52 PM*

**[REMOVED]**
```
(from line ~10)
    print("")
```
**[ADDED]**
```
10        print(f"the current number is")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:41 PM*

**[REMOVED]**
```
(from line ~10)
    printf("")
```
**[ADDED]**
```
10        print("")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:28 PM*

**[REMOVED]**
```
(from line ~9)
for i in range(1 , innput+1):

```
**[ADDED]**
```
9     for i in range(1 , input+1):
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:22 PM*

**[REMOVED]**
```
(from line ~10)
    printf()
```
**[ADDED]**
```
10        printf("")
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:20 PM*

**[REMOVED]**
```
(from line ~10)
    print()
```
**[ADDED]**
```
10        printf()
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:17 PM*

**[REMOVED]**
```
(from line ~10)
    
```
**[ADDED]**
```
10        print()
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:15 PM*

**[REMOVED]**
```
(from line ~9)
for i in range(1 , innput+1)
```
**[ADDED]**
```
9     for i in range(1 , innput+1):
10        
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:11 PM*

**[REMOVED]**
```
(from line ~8)
input = 

```
**[ADDED]**
```
8     input = 19
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:09 PM*

**[REMOVED]**
```
(from line ~8)
int

```
**[ADDED]**
```
8     input = 
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:06 PM*

**[REMOVED]**
```
(from line ~8)


```
**[ADDED]**
```
8     int
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:50:02 PM*

**[REMOVED]**
```
(from line ~9)
for i in range(1 , innput)
```
**[ADDED]**
```
9     for i in range(1 , innput+1)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:59 PM*

**[REMOVED]**
```
(from line ~9)
for i in range(1 )
```
**[ADDED]**
```
9     for i in range(1 , innput)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:55 PM*

**[REMOVED]**
```
(from line ~9)
for i in range()
```
**[ADDED]**
```
9     for i in range(1 )
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:41 PM*

**[ADDED]**
```
9     for i in range()
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:35 PM*

**[REMOVED]**
```
(from line ~9)
i
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:34 PM*

**[REMOVED]**
```
(from line ~9)
i 
```
**[ADDED]**
```
9     i
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:32 PM*

**[ADDED]**
```
9     i 
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:27 PM*

**[ADDED]**
```
7     
8     
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:49:25 PM*

**[REMOVED]**
```
(from line ~1)
total_sum = 0

```
**[ADDED]**
```
1     # total_sum = 0
```
**[REMOVED]**
```
(from line ~3)
for i in range(2, 51, 2):
    total_sum += i

```
**[ADDED]**
```
3     # for i in range(2, 51, 2):
4     #     total_sum += i
```
**[REMOVED]**
```
(from line ~6)
print("Sum of even numbers:", total_sum)

```
**[ADDED]**
```
6     # print("Sum of even numbers:", total_sum)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:43:52 PM*

**[REMOVED]**
```
(from line ~2)
# Step by 2 starting from 2 to hit only even numbers

```
**[ADDED]**
```
2     
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:43:26 PM*

**[REMOVED]**
```
(from line ~1)
x = "GFG"
for i in range(x):
    print(i)
```
**[ADDED]**
```
1     total_sum = 0
2     # Step by 2 starting from 2 to hit only even numbers
3     for i in range(2, 51, 2):
4         total_sum += i
5     
6     print("Sum of even numbers:", total_sum)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop1.py
*Saved at: 7/14/2026, 11:41:39 PM*

**[ADDED]**
```
1     x = "GFG"
2     for i in range(x):
3         print(i)
```

---

### 📄 d:\Vs Code\python-coding-pratice\loops\for loop.py
*Saved at: 7/14/2026, 11:39:54 PM*

**[ADDED]**
```
1     x = 0
2     while x < 100:
3         x += 2
4     print(x)
```

---

