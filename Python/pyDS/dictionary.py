Dictionary_Name={} #symbol method
print(Dictionary_Name)
print(type(Dictionary_Name))
Dictionary_Name=dict()#dict constructor method
print(Dictionary_Name)
print(type(Dictionary_Name))
phone_book={
                'ramu':'1234568790',
                'santhosh':'9325698789',
                'ajay':'6326598752'
           }
print ("phone number:",phone_book['ramu'])
print ("phone number:",phone_book['santhosh'])
phone_book=dict(
                ramu='1234568790',
                santhosh='9325698789',
                ajay='6326598752'
           )
print ("phone number:",phone_book['ramu'])
print ("phone number:",phone_book['santhosh'])
words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
print(words)