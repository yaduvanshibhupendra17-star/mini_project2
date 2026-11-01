# mini_project2

Smart Canteen Billing and Order Analyzer

Project brief
Build a command-line canteen ordering and billing system. It should display a numbered menu, let the user select
items and quantities, calculate the bill, apply a simple discount based on the order total, and print a final receipt. The
program should also support multiple orders in one run and stop when the user chooses to finish.
Learning outcomes
• Use if, if-else, if-elif-else, and nested if statements to validate choices and apply pricing rules.
• Use for loops and range() to display menu items and process a fixed number of item choices.
• Use a while loop to keep accepting order actions until the user chooses to exit.
• Use break to stop the ordering loop, continue to skip invalid selections, and pass to represent a planned but
not-yet-implemented branch where appropriate.
• Use nested loops to print a simple quantity or item summary, and practise number-based logic where useful.

Menu and prices (use these exact values)
Item number Item Price
1 Veg Sandwich ■60
2 Masala Dosa ■80
3 Chole Rice ■90
4 Paneer Roll ■100
5 Tea ■20
Functional requirements
1. Display menu: Print all menu items with item numbers and prices. Use a for loop and range() where suitable.
2. Accept orders: Ask the user to enter an item number and quantity. A valid item number is 1–5. A quantity must be
a positive integer.
3. Validate choices: Use conditional statements to handle invalid item numbers and invalid quantities. Invalid input
should show a helpful message and must not add anything to the bill.
4. Calculate item cost: Calculate each line cost as price × quantity. Add it to the running total.

5. 5. Repeat or finish: Use a while loop to allow more than one item selection. After each valid item, ask whether the
user wants to add another item. Use break when they choose to finish.
6. Apply discount: If the subtotal is ■500 or more, apply a 10% discount. If it is ■250–■499.99, apply a 5%
discount. Otherwise, no discount applies. Use if-elif-else.
7. Print receipt: Display each selected item, quantity, line cost, subtotal, discount amount, and final total.
8. Handle empty order: If the user finishes without adding a valid item, print that no order was placed and do not
apply a discount.
Topics to apply
Module 1 topics may be reused: variables, data types, type conversion, input/output, operators, and basic syntax.
Module 2 topics include conditional statements, nested if, for/while loops, range(), nested loops, break, continue,
pass, and number-based logic.
Required modules and packages
External packages: None.
Python modules: None required. Use built-in functions such as input(), print(), int(), range(), and type() if useful.
