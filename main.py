#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python



#Introduction
print("Welcome to the tip calculator!")
#Input total bill
total_input= float((input("What was the total bill? $")))
#input tip percentage as a string
tip_input = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))
#input amount of people splitting the bill
split_input = int(input("How many people will split the bill? "))
#calculate the tip
tip_pct = tip_input / 100
tip_amount = total_input * tip_pct
total_bill = total_input + tip_amount
#caluclate how much per person
bill_split = round(total_bill / split_input, 2)

print(f"Each person must pay ${bill_split}.")