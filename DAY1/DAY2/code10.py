n=int(input("Enter a number: "))

''''i=1
while(i<=10):
    if(i%6==0):
        break
    print(i)
    i+=1'''

''''i=1
while(i<=10):          #without continue statement
    print(i)
    i+=2'''

i=0
while(i<10):
    if(i%2==0):         #with continue statement
        i+=1
        continue
    print(i)
    i+=1