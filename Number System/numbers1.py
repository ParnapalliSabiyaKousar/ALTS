"""write a program  which will find all numberswhich is divible by 7
but are not a multiple of 5 between 2000 and 3200 (both included) the number obtained should bbe comma separeted sequence in a single line
Hint:consider using a range (#b3gin,#end)method of   5  """
numbers=[]
numbers1=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0 :
        numbers.append(int(i))
print(numbers)
print(','.join(numbers1))




