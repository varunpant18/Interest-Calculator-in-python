principle = 0
rate = 0 
Time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be zero or less than that!")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate cant be zero or less than that!")

while Time <= 0:
    Time = int(input("Enter the Time: "))
    if Time <= 0:
        print("Time cant be zero or less than that!")

total = principle * pow((1 + rate/100), Time)
print(f"Balance after {Time} years is: ₹{total:.2f}.")