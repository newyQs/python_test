a = [1, 2, 3, 4, 5]

i, j = 0, len(a)

while i < j - 1:
    if len(a) < 1:
        break
    if a[i] in [1, 2, 3, 4, 5]:
        a.remove(a[i])
    else:
        i += 1

print(a)
