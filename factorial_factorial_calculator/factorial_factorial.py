import math as mt

n = int(input('Enter a positive number: '))
product = 1

for i in range(n, 0, -1):
    product *= mt.factorial(n)
    
print(f"The product of factorials from {n}! to 1! is: {product}")

# this code calculates the product of factorials from n! to 1!
# i bricked my terminal with 99! lol, 10! gave me an unfathomably large number
# mayhaps the amount of stars in the universe