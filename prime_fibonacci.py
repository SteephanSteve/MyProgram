#!/usr/bin/python

n=input()
c=0
if n==1:
   print '1'
else:
 k=n/2
 if n%2==0:
   i=2
   while i:
       for j in range(2,i):
          if i%j==0:
             break
       else:
          c+=1
          if c==k:
            print i
            break
       i+=1
 else:
   a,b=0,1
   while True:
      s=a+b
      a,b=b,s
      c+=1
      if c==k+1:
         print a
         break
      


