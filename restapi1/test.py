n=[45, 22, 14, 65, 97, 72]
for i in range(len(n)):
    if n[i] % 3 == 0 and n[i]%5==0:
        n[i]="fizzbuzz"
    elif n[i]%3==0:
        n[i]="fizz"
    elif n[i]%5==0:
        n[i]="buzz"
print(n)




