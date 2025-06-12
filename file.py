dict1 = {1: 2, 5: 3, 4: 4}

l = sorted(dict1.values(), reverse=True)  # Sorting values

for i in l:
    for key, value in dict1.items():
        if value == i:
            print(f"{key}: {value}")
            break  # Ensures unique key-value pairs only
