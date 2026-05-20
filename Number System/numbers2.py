"""Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: 
hello world! 123 
Then, the output should be: LETTERS 10 DIGITS 3
Hints: In case of input data being supplied to the question,
nit should be assumed to be a console input."""


"""sentence=input("Enter a sentence:")
letters=0
digits=0
for ch in sentence :
    if ch.isalpha():
        letters+=1
    elif ch.isdigit():
            digits+=1

print("LETTERS",letters)
print("DIGITS",digits)
print("Letters:{},Digits:{}" .format(letters,digits))"""


#using dictionary
sentence=input("Enter a sentence:")
count={"LETTERS":0,"DIGITS":0}

for ch in sentence :
    if ch.isalpha():
        count["LETTERS"]+=1
    elif ch.isdigit():
        count["DIGITS"]+=1
    else:
        pass     
print("LETTERS",count["LETTERS"])
print("DIGITS",count["DIGITS"])
