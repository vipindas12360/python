n=int(input())
a = []
for i in range(n):
    i=int(input())
    a.append(i)
for j in range(n):
    if a[j]>=0:
        print(a[j], end =' ')
