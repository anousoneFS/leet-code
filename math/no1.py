n = 0
for i in range(1, 201):
    if i % 3 == 0 and i % 7 == 0:
        n += 1

print(f"count = {n}")
