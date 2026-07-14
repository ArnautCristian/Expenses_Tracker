from datetime import datetime
import json

# Defining the JSON data saving function
def Save_Expense(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
        
# Defining the loading expenses from the JSON file function
def Load_Expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
expenses = Load_Expenses()

# Defining the "Exit from the app" function
def Exit():
    print ("Bye bye!")
    exit()

# Defining the "return to menu or exit" function for when operations are finished
def Return_Menu():
    next_action = input('To return to the Main Menu type "menu". To exit the app type "exit": ')
    while True:
        if next_action == "menu":
            return
        elif next_action == "exit":
            Exit()
            break
        else:
            while next_action not in ["menu","exit"]:
                next_action = input('Please type only "menu" or "exit": ')
                break
# Expense Tracker
# Defining the app as a function and Menu presentation
def Expense_Tracker():
    print("Welcome to the Expense Tracker!")
    while True:
        print("Actions Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit Expense Tracker")
        action = input("Choose the action you want to make (type 1, 2, 3, 4, 5 or 6): ")
        
        # Menu selection and input validity check
        while True:
            if action not in ["1","2","3","4","5","6"]:
                action = input('Please type either "1" or "2" or "3" or "4", "5" or "6": ')
            else:
                break
        
        
        # Defining the first menu selection as a function
        def Add_Expense():
            while True:
                print("Let's add your expenses! Please complete the below sections in the following formats: [DD-MM-YYYY], [Food], [12.5]")
                Date = input("Date: ")
                # Checking if the user's input is a valid date
                while True:
                    try:
                        datetime.strptime(Date, "%d-%m-%Y")
                        break
                    except ValueError:
                        Date = input('Please type a valid date (DD-MM-YYYY): ')
                Category = input("Category: ")
                # Chekcing if the user's input is a valid one-word string
                while True:
                    if Category.isalpha():
                        break
                    else:
                        Category = input("Please enter only one word for this category: ")
                Amount = input("Amount: ")
                # Checking if the user's input is a valid float
                while True:
                    try:
                        Amount = float(Amount)
                        break
                    except ValueError:
                        Amount = input('Please enter a valid amount: ')
                expense = {
            "Date": Date,
            "Category": Category,
            "Amount": Amount
        }  
                expenses.append(expense)
                Save_Expense(expenses)
                next_action = input('Do you want to add another expense? Type "yes" to add another expense or "no" to return to the main menu: ')
                while True:
                    if next_action == "yes":
                        break
                    elif next_action == "no":
                        return
                    else:
                        while next_action not in ["yes","no"]:
                            next_action = input('Please type either "yes" or "no": ')
                            break
                        
                 
        # Defining the second menu selection as a function
        def View_All_Expenses():
            print(f"{'Date':<12}{'Category':<15}{'Amount':<10}")
            print("-" * 37)
            for expense in expenses:
                print(f"{expense['Date']:<12}{expense['Category']:<15}€{expense['Amount']}")
            Return_Menu()
                    
        
        # Defining the third menu selection as a function            
        def View_Total_Spent():
            total = 0 
            for expense in expenses:
                total +=expense["Amount"]
            print(f"Total spent: €{total:.2f}")
            Return_Menu()
                    
        
        # Defining the fourth menu selection as a function            
        def Search_Expense():
            while True:
                search = input("Enter the category you are looking for: ")
                found = False
                for expense in expenses:
                    if expense["Category"] == search:
                        print(expense)
                        found = True
                if found:
                    break
                search = input("Type a word that is present within the previously entered categories: ")
            Return_Menu()
            
        #Defining the delete expenses function    
        def Delete_Expense():
            while True:
                print ("These are the currently saved expenses:")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense['Date']} | {expense['Category']} | €{expense['Amount']:.2f}")
                while True:
                    try:
                        choice = int(input("Enter the number of the expense to delete: "))
                        while choice < 1 or choice > len(expenses):
                            choice = int(input("Please enter a number present in the list: "))
                        break
                    except ValueError:
                        while True:
                            try:
                                choice = int(input("Please enter a valid number: "))
                                break
                            except ValueError:
                                pass
                expenses.pop(choice - 1)
                Save_Expense(expenses)
                if len(expenses) == 0:
                    print("There are no expenses left. You will be redirected to the main menu.")
                    return
                print ("Here's the updated expenses list:")
                for i, expense in enumerate(expenses, start=1):
                    print(f"{i}. {expense['Date']} | {expense['Category']} | €{expense['Amount']:.2f}")
                next_action = input('Do you want to delete another expense? Type "yes" to delete another expense or "no" to return to the main menu: ')
                while True:
                    if next_action == "yes":
                        break
                    elif next_action == "no":
                        return
                    else:
                        while next_action not in ["yes","no"]:
                            next_action = input('Please type either "yes" or "no": ')
                            break
        

                    
        # Redirecting the user to the action they choose from the menu            
        if action == "1":
            Add_Expense()
        elif action == "2":
            View_All_Expenses()
        elif action == "3":
            View_Total_Spent()
        elif action == "4":
            Search_Expense()
        elif action == "5":
            Delete_Expense()
        elif action == "6":
            Exit()



Expense_Tracker()
