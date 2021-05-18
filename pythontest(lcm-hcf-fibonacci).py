#!/usr/bin/env python
# coding: utf-8

# In[5]:


#number is armstrong or not
num=153
sum=0
for i in str(num):
    sum+=int(i)**3
print(sum)    
if num==sum:
    print(f"{num} is armstrong")
else:
    print(f"{num} is not armstrong")


# In[7]:


#find LCM

num=12
num2=4

maxnum=max(num,num2)
while(True):
    if maxnum%num==0 and maxnum%num2==0:
        break
    maxnum=maxnum+1
print(f"the lcm of {num} and {num2} is {maxnum}")  
    


# In[12]:


# find HCF for two number

num=12
num2=4
hcf=1
maxnum=max(num,num2)
for i in range(1,maxnum+1):
    if num%int(i)==0 and num2%int(i)==0:
        hcf=i

print(f"the hcf of {num} and {num2} is {hcf}") 


# In[18]:


#fibonacci  series

def fibonaccis(n):
    prenum=0
    currentnum=1
    for i in range(1,n):
        preprenum=prenum
        prenum=currentnum
        currentnum=preprenum+prenum
    return currentnum

fibonaccis(4)
    

