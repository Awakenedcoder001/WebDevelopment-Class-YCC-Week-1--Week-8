#write a program to check if a year is a leap year or not

n = 365
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")
