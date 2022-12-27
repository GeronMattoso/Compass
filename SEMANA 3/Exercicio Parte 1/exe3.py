def evenOdd(num:int):
    if (num%2==0):
        return 1
    else:
        return 0

for num in range(0, 21):
    if(evenOdd(num)):
        print(num)