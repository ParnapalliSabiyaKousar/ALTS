f=open("Book.txt","r")
print(f.read())
print(type(f))
print(f)
f.close()


f=open("Book.txt","r")
str=f.readlines()
print(type(str))
print(str)
f.close()

f =open("Book.txt","r")
for x in f:
    print(x)
f=open("Book.txt","r")
lines=f.read().splitlines()
print(type(lines))
print(lines)
f.close()

with open ("Book.txt","r") as f:
  lines=f.read().splitlines()
  print(type(lines))
  print(lines)
  f=open("Book.txt","r")

str=f.read()
L=str.split()
count_char=0
for i in L:
    count_char=count_char+len(i)
print(count_char)
f.close()
