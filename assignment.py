# a programme to check whether a year
# is a leap year or not

year = 2022
year1 =2024
if year %  4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          print("year is a leap year")
        else:
            print("year is not a leap year")

    else:
        print("year is a leap year")
else:
    print("year is not a leap year")


if year1 % 100 == 0:
    if year1 % 400 == 0:
        if year1 % 4 == 0:
          print("year is a leap year")
    else:
        print("year is not a leap year")
else:
     print("year is  a leap year")


# a program to check whether a letter is a
# consonant or a vowel
vowel = "AEIOUaeiou"
letter = "t"
if letter in vowel:
    print("letter is a vowel")
else:
    print(letter, "is consonant")

