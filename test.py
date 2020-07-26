def position(num):
  b=num
  a=[0]*len(num)
  count=0
  while(a!=num):
    count++
    a=[0]*len(num)
    for i in range(len(num)):
      a[num[i]-1]=b[i]
     b=a
    return count
  n=int(input())
  for i in range (n):
    number=int(input())
    monkey=list(map(int,input().split()))
    r=position(monkey)
    print(r)
a=10
