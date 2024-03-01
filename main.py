num = input('Enter a number (decimal only): ')
# type your code here
deci = num.find(".")
num2 = num[deci+1:]
dp = len(num2)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
