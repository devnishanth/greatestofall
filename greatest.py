list=[]
largest=0
smallest=0
while True:
    num = input("Enter a number: ")
    if num != "done":
        try:
            int(num)
            list.append(int(num))
        except:
            print("Invalid input")
    else:
        break
print(list)
largest = max(list)
smallest = min(list)
print("Maximum is ", largest)
print("Minimum is ",smallest)
