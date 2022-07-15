print("how many elements in list you want to be")
p = int(input())
l=[]
for i in range(p):
    k = int(input())
    l.append(k)

print("even numbers that are multiplied by 2 are below")
for items in l:
    
    if items % 2 == 0:
        end = items*2
        print(end)
