f=open('avin.txt','r')
f1=open("a.txt","w+")
str=f.readlines()
print(str)
for i in range(len(str)):
    if i%2==0:
        print(str[i])
        f1.write(str[i])
        f1.write("\n")
f1.seek(0,0)
a=f1.read()
print(a)
f1.close()
f.close()"""
#sol 2
"""f=open('avin.txt','r')
f1=open('a.txt','w+')
str=f.read().split()
print(str)
for i in range(len(str)):
    if i%2==0:
       print(str[i])
       f1.write(str[i])
       f1.write(' ')
f1.seek(0,0)
a=f1.read()
print(a)
f1.close()
f.close()"""
#sol 3
"""f=open('avin.txt','r')
s=n=t=0
str=f.read()
for i in str:
    if ord(i)==32:
        s+=1
    elif i=='\n':
        n+=1
    elif i=='\t':
        t+=1
print(s,n,t)
f.close()"""
