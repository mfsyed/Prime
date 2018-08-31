

number = int(input("Pick a number between 1 and 100 and we'll let you know if it's prime."))

count = 1
divide = 1


for i in range(1,number):
    if number%i == 0:
        count = count + 1
        factor = (number/i)
        print(str(factor) + " x " + str(i) + " is " + str(number))
        
        
        
if count == 2:
    print("Your number is prime.")

if count != 2:
    print("Not Prime.")
