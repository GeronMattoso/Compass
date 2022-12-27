def yearTo100(name:str, age:int):
    result = 2022 + (100 - age)
    return result

name  = str(input("Name:"))
age = int(input("Age:"))

print("100 years in: {} " .format(yearTo100(name, age)))
