n = int(input("enter a number:"))
start = int(input("enter the number from which you want to start:"))
end = int(input("enter the number from which you want to end:"))
for i in range (start,end+1):
    print(n,"x",i,"=",n*i)