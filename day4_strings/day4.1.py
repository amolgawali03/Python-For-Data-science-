""" string methods """

# name=input("enter a string:")
phone_num=(input("enter a phone number:"))

# result=len(name) # it also counts space 
# result=name.find("o") # will find the first occurance of o in the string ( follows indexes)
# result=name.rfind("o") # will find the first occurance of o in the string checking from last item ( follows indexes)
# result=name.rfind("s") # rfind method will return -1 if the value is not present in the string
# name=name.capitalize() # will capitalize the first letter of the sring
# name=name.upper() # will convert all the letters in the sting into upper case 
# name=name.lower() # will convert all the letters in the sting into lower case
# result=name.isdigit() # will return true only if the string contains only numbers 
# result=name.isalpha() # will return true only if the string contains only alplabates . note string should contain no spaces 
# result =phone_num.count("-")
result=phone_num.replace("-","")
print(result)