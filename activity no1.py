def armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum__powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum__powers == num
num = int(input("Enter a number: "))
if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
