
#Name = str(input("What is your name ? :"))
#print ("Your name backwards is ") 
#temp_name = '' 
#for i in Name[::-1]:
 #   temp_name += i

#print(temp_name)





User_Name = str(input("What is your name ?: "))

def Name_Backwards(User_Name):
    Final_Name = ''
    for i in User_Name[::-1]:
        Final_Name += i    


    return Final_Name 

print(Name_Backwards(User_Name))   