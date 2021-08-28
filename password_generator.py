import random
print("The generated password having 10 characters is : ")
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="!@#$%^&*"
s3="1234567890"
s4="abcdefghijklmnopqrstuvwxyz"
s5=s1+s2+s3+s4;
upper_string=random.choice(s1)#It ensures at least 1 upper case character
lower_string=random.choice(s4)#It ensures at least 1 lower case character
symbol=random.choice(s2)#It ensures at least 1 special symbol
digit=random.choice(s3)#It ensures at least 1 digit
temp_password=upper_string+lower_string+symbol+digit
password=''.join(random.sample(temp_password,len(temp_password)))#ut shuffles the 4 charcters
x=1;
while x<=8:#getting the rest 8 characters
    sr = ''.join(random.sample(s5,len(s5)))#shuffling
    password+=random.choice(sr)
    x+=1
password=''.join(random.sample(password,len(password)))#Again shuffling to ensure the password is strong
print(password)

