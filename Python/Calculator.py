cons=True
func=["+","-","%","X"]

def TakingInput():
    num1=int(input())
    # calc=input()
    num2=int(input())
    return num1,num2

def Display(a,b,c):
    print("{} {} {} = {}".format(a,b,c,a+b))

x=TakingInput()
print(x().num1)
# Fun2=Display()
# i=TakingInput().num1
# j=TakingInput().num2
# p=TakingInput().calc

# Display(i,j,p)