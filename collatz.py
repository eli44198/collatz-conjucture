"""
calculating the sequence in python
"""

def collatz(num):
  if num<=1:
      return 1
  res=[]
  while num!=1:
    if num%2 == 1:
      num*=3
      res.append(num+1)
    else:
      num/=2
      res.append(num)
      
   return res
   
t=input()
while t:
  collart(t)
