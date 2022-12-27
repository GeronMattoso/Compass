def parImpar(num:int):
    if num%2==0:
        result = "Par"
    else:
        result = "Impar"
    return result

num = int(input("number:"))

print(parImpar(num))

