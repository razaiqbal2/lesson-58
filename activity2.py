def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)

n=float(input('Enter your numbers : '))
print('the factors of ', n, 'are')
print(n)