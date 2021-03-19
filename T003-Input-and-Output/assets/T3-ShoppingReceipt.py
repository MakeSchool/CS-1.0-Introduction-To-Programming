# Shopping Receipt

# Shopping Cart Setup
username = 'Joi'
item_1 = 2      # $2
item_2 = 10     # $10
item_3 = 11     # $11
cart_total = item_1 + item_2 + item_3

# Step 1: In the new version of Python, we can use f-string syntax as an easier way to print variables in sentences without needing to use type casting. Take a look at the f-string to print the cart total and run the program to see what happens!
print(f"{username}'s cart balance is {cart_total}")

# Step 2: You can even use expressions in your f-string! Update the f-string from Step 1 to add 5 dollars to the cart_total with the expression 5 + cart_total in the curly braces. Test your update by running the program again.

# Step 3: The minimum for free shipping at your online store is $25. Use the f-string syntax to print a message telling the user how much they need to add to their cart total to qualify for free shipping. For example: "Joi, you are $2 away from free shipping!".