import random
import string
print("WELCOME TO PASSWORD GENERATOR")
passw = []

while True:
    try:
        n = int(input("Enter the length of password greater that 8: "))
        if n >= 8:
            break
        else:
             print("Please enter number greater than 8 for stronger password!")

    except ValueError:
        print("Please enter a valid number.")



print("Do you want to ")
x=[]
i=0
while True :
    
    if "y" not in x:
        if i>0:
            print("Please select atleast one character!")
        upper=input("Include uppercase letters?(y/n): ")
        lower=input("Include lowercase letters?(y/n): ")
        digits=input("Include digits letters?(y/n): ")
        special=input("Include special characters letters?(y/n): ")
        x=[upper,lower,digits,special]
    else:
        break
    i+=1

if upper == "y":
    passw.append(string.ascii_uppercase)
if lower == "y":
    passw.append(string.ascii_lowercase)
if digits == "y":
    passw.append(string.digits)
if special == "y":
    passw.append(string.punctuation)


gen_list=[]
k=len(passw)


while k != 0:
    k-=1
    if (passw[k] == string.punctuation) or (passw[k] == string.digits) : 
        gen_list.extend([random.choice(passw[k]) for i in range(3)])
    else:
        gen_list.extend([random.choice(passw[k]) for i in range(n-3)])


generated_pass = [random.choice(gen_list) for i in range(n)]
gen_cpy = generated_pass.copy()
alp_chk=1
for i in generated_pass:
    if i.isalpha() and (alp_chk < 4) :
        gen_cpy.remove(i)
        gen_cpy.insert(0,i)
        alp_chk+=1
    elif not i.isalnum():
        gen_cpy.remove(i)
        gen_cpy.append(i)
     

generated_pasx = "".join(gen_cpy)
print("\n✅ Generated Password:", generated_pasx)



    
        
