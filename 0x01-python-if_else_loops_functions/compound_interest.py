#!/usr/bin/python3

def compound_interest(amount, interest):
    interest_calc = 1 + (interest / 100)
    total = amount
    for i in range(0, 10):
        total *= interest_calc
    return (total)

amount_input = input("Enter the amount of money to be invested: ")
interest_input  = input("Enter the interest rate: ")
amount = eval(amount_input)
interest = eval(interest_input)
total = compound_interest(amount, interest)

print(f"\n\nAmount invested is: {amount}\nYearly interest rate: {interest}\nAmount after investment over a 10 year period: {total:.2f}")
