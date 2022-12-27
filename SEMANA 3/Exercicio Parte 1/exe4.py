def main():
    for num in range(0, 101, 1):
        if(primo(num)):
          print(num)

def primo(num:int):
    primos = []

    for a in range(1, num + 1, 1):
        if num%a==0:
            primos.append(a)#counter

    if len(primos)==2:
        return 1
    else:
        return 0

main()
