x = 1

while x < 6:
    print(x)
    if x == 3:
        break
    x += 1
    
y = 0

while y < 6:
    y += 1
    if y == 3:
        continue
    print(y)