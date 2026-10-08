#1
r = float(input("Enter the radius of the circle? "))
s = 3.14 * r**2
print(f"Circle area = {s}")
#2
r = int(input("Enter the temperature in Celsius: "))
f = (r * 9/5) + 32
print(f"{r} (C) = {f} (F)")
#3
n = int(input("Enter a number? "))

for i in range(2, n):
     if n % i == 0:
        print(f"{n} is a NOT prime number")
        break
if i == n-1:
    print(f"{n} is a NOT prime number")
#4
n = int(input("Enter a number? "))
s = 0 
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT a perfect number")
#5
n = ["Blue", "Red", "Green"]
r = input("What is your favorite color? ")
if r in n:
    index = n.index(r)
    print(f"Your color is at index {index} in my list")
else:
    print(f"Sorry,I couldn't find your color")
#6
print("\nRange 1:")
for n in range(7):
    print(n)

print("\nRange 2:")
for n in range(1, 11, 3):
    print(n)

print("\nRange 3:")
for n in range(5, 0, -1):
    print(n)

print("\nRange 4:")
for n in range(6, -3, -2):
    print(n)
#7
def remove_dollar_sign(s):
    return s.replace("$", "")
print(remove_dollar_sign("Hello Worl$$$$d"))

#8
I = [1,4,5,-1,10]
print(I)
r = [val for val in I if val % 2 == 0]
print(r)
#9
def factorial(n):
    r=1
    for i in range(2, n + 1):
        r *= i
    return r
print(factorial(5))  
print(factorial(0))  
#10
num = int(input("Enter a number: "))
divisors = []
for i in range(1, num + 1):
    if num % i == 0:
        divisors.append(i)
print(f"Divisors of {num}: {divisors}")
#11
import math

def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2))

print("%.6f"%distance(3, 4, 4, 3))
#12
def pattern(m, n):
    for i in range(m):
        
        if i == 0 or i == m - 1:
            print("*" * n)
        
        else:
            if n > 1:
                print("*" + " " * (n - 2) + "*")
            else:
                print("*")

pattern(4, 5)
