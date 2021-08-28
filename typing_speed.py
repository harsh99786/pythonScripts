import matplotlib.pyplot as plt
import time as t

import random
word_list=["Programming","Environment","Coding","Aptitude","Hashing","Sorting","Searching","LinkedList","Array","Instrumentation","Electrical","Random","Local"]
index=random.randint(0,(len(word_list)-1))
random_word=word_list[index]
print("You have to type the word ", random_word ," five times.")
input("Press enter to continue :")
x=0
mistakes=0
timetaken=[]
while x<5:
    start=t.time()
    word=input("Type the word  :  ")
    end=t.time()
    timetaken.append(round((end-start),4))
    if(word!=random_word):
         mistakes+=1
    x+=1     
print("You took the following times to type the word everytime ")
print(timetaken[0:])
print(" You typed ",mistakes," times wrong ")
X=[1,2,3,4,5]
Y=timetaken
plt.plot(X,Y)
legend=["1","2","3","4","5"]
plt.xticks(X,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Number of attempts")
plt.title("Your typing evolution")
plt.show()





