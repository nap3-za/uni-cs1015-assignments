# Spam message generator
# Date: 22 February 2024

first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
sum_of_money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

thirty_percent_money = round((sum_of_money*0.3), 1)

print("\nDearest " + first_name + "\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk "+ last_name + ", your long lost relative from Mapsfostol.\nMy father left the sum of " + str(sum_of_money) + "USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in "+country+".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - " + str(thirty_percent_money) + "USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank "+last_name)
