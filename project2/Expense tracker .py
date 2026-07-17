def expense_tracker():
    expenses = {}


    while True :
        category=input("enter expense category (type 'quit'to exit):").lower()
        if category == "quit":
            break
        amount=float(input("enter expense amount : "))
        if category in expenses:
            expenses[category]+=amount
        else:
            expenses[category] = amount
    print("expenses :")
    for category ,amount in expenses.items():
        print(f"{category.capitalize()} : ${amount:.2f}")     

expense_tracker()               
