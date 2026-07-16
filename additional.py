from collections import Counter

def merge_inventories(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

store_a = {'apples': 10, 'bananas': 5, 'oranges': 8}
store_b = {'bananas': 12, 'oranges': 2, 'grapes': 15}

combined = merge_inventories(store_a, store_b)
print("Merged Inventory:", combined)
