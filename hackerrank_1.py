n = int(input())
lst = [int(x) for x in input().split(" ")]
lst.sort(reverse = True)
t = max(lst)
lst.remove(t)

for i in range(11):
    if t in lst:
        lst.remove(t)
print(lst[0])
