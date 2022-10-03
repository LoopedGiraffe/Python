total = 0

for num in range(2,101,2):
    total += num

print(total)

#another way:
tot = 0
for numb in range(1,101):
    if numb % 2 == 0:
        tot += numb

print(tot)