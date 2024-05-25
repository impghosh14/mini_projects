import random 

x=random.randint(1,100)
# print("Computer chose {}".format(x))
a=int(input("Chose a number in between 0 to 100::"))
score=10
j=1
for i in range (2,10):
    if(a>x):
        a=int(input("Chose a Small Number then {}::".format(a)))
    elif(x>a):
        a=int(input("Chose a Large Number then {}::".format(a)))
    else:
        break
    score=10-i
    j=i
if(a==x):
    print("Congrats!! you have schose correct Number in {} attempts which is {}".format(j,x))
    print("Your Score is {}".format(score))
else:
    print("Sorry!! You have reached maximum attempts")


