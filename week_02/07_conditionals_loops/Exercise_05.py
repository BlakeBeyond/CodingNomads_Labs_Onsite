'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
'''


#add

lower = int(input("type a number "))
upper = int(input ("type a higher number ")) + 1
total = 0

for num in range(lower, upper):
    total += num

count = upper / lower
average = total / count

print(total, average)