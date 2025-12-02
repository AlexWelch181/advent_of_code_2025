c = 50
out = 0

with open('day_one_in.txt') as file:
    data = [(line[0], int(line[1:])) for line in file]

for d, u in data:
    step = 1 if d == 'R' else -1
    for _ in range(u):
        c = (c + step) % 100
        if c == 0:
            out += 1
        
print(out)
