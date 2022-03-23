# 1. Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print out the sentence on one line using print.
a = 'All'
b = 'work'
c = 'and'
d = 'no'
e = 'play'
f = 'makes'
g = 'Jack'
h = 'a'
i = 'dull'
j = 'boy'


print(a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + ' ' + g + ' ' + h + ' ' + i + ' ' + j + '.')

#-------------------------------------------------------------------------------------------------------------------------------------------

# 2.Add parenthesis to the expression 6 * 1 - 2 to change its value from 4 to -6. 
6 * (1 - 2)

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 3. Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as: “Hello Eric, would you like to learn some Python today?”
name = 'Joshua'

print(name + ", let's learn some Python today!!")

#----------------------------------------------------------------------------------------------------------------------------------------

# 4. Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
print('Elon Musk, the CEO of Tesla Inc. once said, "Everybody should learn to program a computer, because it teaches you to think."')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
famous_person = "Elon Musk"
message = "Everybody should learn to program a computer, because it teaches you how to think."

print(famous_person + ', the CEO of Tesla Inc. once said, ' + message)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
fave_number = 7
msg = "My favorite number is " + str(fave_number)

print(msg)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 7. Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years.
p = 10000
n = 12
r = 0.08
year = input("Year: ")
t = int(year)

final_amount = p * ((1 + r / n) ** (n * t))

print(final_amount)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Write a Python program that gets the amount of electricity used in kilowatt-hours and the cost of electricity per kilowatt-hour. Compute and display the total amount of the electric bill, including an 8% sales tax.
sales_tax = 0.08
elect_used = input("Enter amount of electricity used in (kW-h): ")
cost = input("Enter cost of electricty/kW-h: ")

total_amount = float(elect_used) * float(cost) * sales_tax

print("Total amount of the electric bill: " + str(total_amount))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Write a Python program that asks for three numbers corresponding to the number of times a race car driver has finished first, second, and third. The program will compute and display how many points the race car driver has earned given 5 points for a first place, 3 points for a second place, and 1 point for a third place finish.
print("Input number of times a race car driver has finished:")
first = input("First: ")
second = input("Second: ")
third = input("Third: ")

compute_points = (int(first) * 5) + (int(second) * 3) + int((third) * 1) 
print("Total points: " + str(compute_points))

# 10. You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask for the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.
time_now_str = input("What time is it (in hrs.)?: " )
time_now = int(time_now_str)
hours_to_wait_str = input("How long to wait (in hrs.)?: " )
hours_to_wait = int(hours_to_wait_str)
time_off = (hours_to_wait % 24) + time_now
print("Time alarms off in : " + str(time_off) + " hrs.")

