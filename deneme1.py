cola=1
chocolate=2
x=int(input("Please enter the number : "))
isDone=False
while not isDone :
    if x==cola :
        print("Take your cola.")
        x=int(input("Please enter the number : ")) 
    elif x==chocolate :
        print("Take your chocolate.")
        x=int(input("Please enter the number : "))
    elif x==0 :
        isDone=True
        print("Closing...")
    else :
        print("Please try again.")
        x=int(input("Please enter the number : "))

