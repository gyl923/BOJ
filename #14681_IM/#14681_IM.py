#1
""" x = int(input())
y = int(input())

if x>0 and y>0:
    ans = 1
elif x<0 and y>0:
    ans = 2
elif x>0 and y<0:
    ans = 4
else :
    ans = 3
print(ans) """

#2
x = int(input())
y = int(input())
if x > 0:
    print(1 if y > 0 else 4)
elif x < 0:
    print(2 if y > 0 else 3)