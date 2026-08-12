import json
import uuid
import datetime

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
         print("Invalid JSON syntax: , Please check the json file and fix the syntax: ", e)


    except Exception as e:
        print("Some Error Occured: ", e)
        return expense_list

def save_expenses(expenses):
    try:
        with open("expenses_details/full_details.json", "w") as file:
            json.dump(expenses, file, indent=4)
                
    except FileNotFoundError:
        open("expenses_details/full_details.json", "x")
        json.dump(expenses, "expenses_details/full_details.json", indent=4)


def print_expense_list():
    try:
        expenses = load_expenses()
        
        # Get the current list from JSON and put it into expense_list
        for i in range(0,len(expenses)):
            print(f"Id: {expenses[i]["Id"]} | Name: {expenses[i]["Title"]} | Date: {expenses[i]["Date"]} | Amount You spend for this: {expenses[i]["Amount"]}")

    except Exception as e:
        print("Some error occured" ,e)
      

def add_expense():

    try:
        print("===============================ADD EXPENSES===================================")
        # Get inputs from the CLI
        title = str(input("Please enter the expense name/title: "))
        month = int(input("Enter the month as number(1-12): "))
        date1 = int(input("Enter the date(1-31): "))
        year = int(input("Enter the year: "))

        date_ = str(datetime.date(year,month,date1))
        
        amount = float(input("Enter the amount you spent: "))
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
    except ValueError as e:
        print("Your typed output is not correct. Please try again: ",e)
    except Exception as e:
        print("Some error Occured: ", e)

def view_expenses_list():
    print("===============================TOTAL EXPENSES===================================\n")
    print_expense_list()

    print("\n================================================================================")

def get_total_spent_amount():
    print("=========================TOTAL AMOUNT SPEND SO FAR==============================")
    expense_list = load_expenses()
    total_amount = 0.0
    for j in range(0,len(expense_list)):
        total_amount += expense_list[j]['Amount']


    print(f"Total Amount you spend so far is: {total_amount}")

    print("================================================================================")

def delete_expense_from_list():
    try:
        print("===============================DELETE EXPENSES===================================\n")
        
        # show list for user to see id and other details
        print_expense_list()

        deleted_item_id = str(input("\nPlease enter id of item that you want to delete: "))
        expense_lists = load_expenses()
        is_entered_id_exist = False
        
        for i in range(0,len(expense_lists)):
            if(str(expense_lists[i]['Id']) == deleted_item_id):
                expense_lists.pop(i)
                is_entered_id_exist = True
                break
        save_expenses(expense_lists)
    
        if(is_entered_id_exist):
            print("=================================DELETED SUCCESSFULLY=============================")
        else:
            print("Your Entered Item is not on the list")
    except Exception as e:
         print("Error Occured: ", e)

def delete_all_expenses():
    print("===============================DELETE ALL EXPENSES===================================\n")
    try: 
        confirm = input("Please type \"confirm\" to delete all current expenses from your list: ")
    except ValueError:
         print("Your typed output is invalid!")
    except Exception as e:
         print("Error Occured: ", e)
    if(confirm == "confirm"):
        expense_list = load_expenses()
        expense_list.clear()

        save_expenses(expense_list)

        print("=================================DELETED ALL EXPENSES SUCCESSFULLY=============================\n")
    else:
         print("You didn't confirm from your side to delete all expenses. Please try again\n")
