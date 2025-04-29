#define simple interest formula
def simple_interest(x,y,z):
    si=(x*y*z)/100
    return si

#user input
p=int(input("Please enter your principal:"))
r= int(input("Please enter your interest rate:"))
t= int(input("Please enter the payment period:"))

simple_interest(p,r,t)
result=simple_interest(p,r,t)
print("This is your interest:", result)