#Write a set of conditional statements to find whether or not a number is a “special” number

#Special numbers are defined as numbers less than 100 or greater than or equal to 300 that are perfectly divisible by 3, 7, or both

# Print out “Divisble by both” if special number divisible by both 3 & 7

# Print out “Divisble by 3” if special number divisible by 3, but not 7

# Print out “Divisible by 7” if special number divisible by 7, but not 3

#Print out “Not a special number” otherwise

number = 356

if number < 100 or number > 300:
    if number%3 == 0 and number%7 == 0:
        print("divisible by both 3 and 7")
    elif number%3 == 0 and number%7 != 0:
        print("divisible by 3,but not 7")
    elif number%7 == 0 and number%3 !=0:
        print("divisible by 7, but not 3")
    else:
        print("Not a special number")
else:
    print("Not a special number")
