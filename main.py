#var = -2 #int
#a = 3.14 #float
#string = 'My text' #string
#boolean = True #sau False = 0


#print(var)
#print(a)
#print(string)
#print(boolean)

#print(var , string)


#print(boolean + var)
#print(boolean - var)
#print(boolean * var)
#print(boolean / var)


#print(4/2) #int
#print(4/3) #float




#value_int = int(input("Enter a int\n") #int
#value_float = float(input("Enter a float\n") #float
#value_string = input("Enter a int\n")  #string
#value_boolean = bool(input("Enter a boolean\n")  #boolean
#print(value_int)
#print(value_float)
#print(value_string)
#print(value_boolean)



#str_var = "4"

#print(int(str_var))

#print(float(str_var))

#print(bool(str_var))



#major = 18
#var_input = int(input("Enter a number"))

#if major < var_input : #Condition 1
    #print("<") #True
#elif major == var_input: #Condition 2
   #print("=")
#else: #Else
   #print(">") #Flase



#var1 = "string"
#var2 = input ("Wassuup\n")


#if var1 == var2:
    #print("12")
#else:
    #print("12")


#for count in range(-10, 10):
    #print(count)


#var = 1
#while var < 100:
    #print(var) #99
    #var = var + 10 #Manual_Increment


import random

var_check = random.randint(0, 25)
var_in = int(input("Enter a number\n"))

while var_in != var_check:
    if var_in > var_check:
        print("Less then need\n")
    else:
        print("More than need")
    var_in = int(input("Enter a number"))
else:
   print("Cong")


