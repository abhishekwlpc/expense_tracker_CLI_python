import json
import uuid
import datetime
import custom_exceptions


def load_expenses():
    expense_list = []
    try:  
        # Get the current list from JSON and put it into expense_list
        with open("expenses_details/full_details.json", "r") as file1:
            expense_list = json.load(file1)
        return expense_list

    except FileNotFoundError:
        return expense_list
    
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON. Error: {e.msg}")
        print(f"Error occured at line {e.lineno}, column {e.colno}")
        pass

def save_expenses(expenses):
        with open("expenses_details/full_details.json", "w") as file:
            json.dump(expenses, file, indent=4)
                


def print_expense_list():

    expenses = load_expenses()
    
    # Get the current list from JSON and put it into expense_list
    for item in expenses:
        print(item)

def add_expense():

    try:
        print("===============================ADD EXPENSES===================================")
        # Get inputs from the CLI

        title = str(input("Please enter the expense name/title: "))
        if(title.isspace() or title == ""):
            raise custom_exceptions.InvalidTextError("Title can not contain spaces or can not be empty")
        
        month = int(input("Enter the month as number(1-12): "))
        date1 = int(input("Enter the date(1-31): "))
        year = int(input("Enter the year: "))

        date_ = str(datetime.date(year,month,date1))
        
        amount = float(input("Enter the amount you spent: "))

        if(amount <= 0):
            raise custom_exceptions.InvalidAmountError("Amount can not be 0 or negative!")
        
        ide = str(uuid.uuid4())


        # Store newly added user data in a dictionary and put it into expense_list
        one_expense={
                "Id" : ide,
                "Title": title,
                "Date" : date_,
                "Amount":amount
        }

        expense_list = load_expenses()
        expense_list.append(one_expense)
        save_expenses(expense_list)


        print("=================================ADDED SUCCESSFULLY=============================")

    except custom_exceptions.InvalidTextError as e:
        print("Caught an error: ", e)
    except custom_exceptions.InvalidAmountError as e:
        print("Caught an error: ", e)
    except ValueError as e:
        print("Your typed output is not correct. Please try again: ",e)


def view_expenses_list():
    print("===============================TOTAL EXPENSES===================================\n")
    print_expense_list()

    print("\n================================================================================")

def get_total_spent_amount():
    print("=========================TOTAL AMOUNT SPEND SO FAR==============================")
    expense_list = load_expenses()
    total_amount = 0.0
    for item in expense_list:
        total_amount += item['Amount']

    print(f"Total Amount you spend so far is: {total_amount}")

    print("================================================================================")

def delete_expense_from_list():

        print("===============================DELETE EXPENSES===================================\n")
        expense_list = load_expenses()
        if(len(expense_list) != 0):

        # show list for user to see id and other details
            print_expense_list()
    
            deleted_item_id = str(input("\nPlease enter id of item that you want to delete: "))
            is_entered_id_exist = False              
            
            for index, item in enumerate(expense_list):
                if(str(item['Id']) == deleted_item_id):
                    expense_list.pop(index)
                    is_entered_id_exist = True
                    break
        
            if(is_entered_id_exist):
                save_expenses(expense_list)
                print("=================================DELETED SUCCESSFULLY=============================")
            else:
                print("Your Entered Item is not on the list")
        else:
            print("No expenses available to delete!")


def delete_all_expenses():
    print("===============================DELETE ALL EXPENSES===================================\n")
    expense_list = load_expenses()
    if(len(expense_list) == 0):
        print("No expenses available to delete!")
    else:
        confirm = input("Please type \"confirm\" to delete all current expenses from your list: ")
        
        if(confirm == "confirm"):
            expense_list.clear()

            save_expenses(expense_list)

            print("=================================DELETED ALL EXPENSES SUCCESSFULLY=============================\n")
        else:
            print("You didn't confirm from your side to delete all expenses. Please try again\n")
