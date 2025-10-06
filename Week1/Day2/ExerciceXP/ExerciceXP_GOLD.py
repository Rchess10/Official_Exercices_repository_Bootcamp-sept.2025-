# #Exercise 1: What is the Season?
# Month = input("Enter the month: ").lower()
# if Month in ["december", "january", "february"]:
#     season = "Winter"
# elif Month in ["march", "april", "may"]:
#     season = "Spring"
# elif Month in ["june", "july", "august"]:
#     season = "Summer"
# elif Month in ["september", "october", "november"]:
#     season = "Autumn"
# print(f"The season is {season}.")

#Exercise 2: For Loop
for i in range(1, 21): 
    print (i)

numbers = list(range(1, 21))
for index, value in enumerate(numbers):
    if index % 2 == 0:
        print(value) 

#Exercise 3: While Loop

