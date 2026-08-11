import json
import uuid
import datetime

# Store in a list
expense_list = []

def get_current_expenses_from_json():
    try:
        expense_list.clear()

        # Get the current list from JSON and put it into expense_list
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                expense_list.append(items[i])
    except Exception as e:
        print("Some Error Occured: ", e)

def print_expense_list():
    try:
        expense_list.clear()
        
        # Get the current list from JSON and put it into expense_list
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                expense_list.append(items[i])
                print(f"Id: {items[i]["Id"]} | Name: {items[i]["Title"]} | Date: {items[i]["Date"]} | Amount You spend for this: {items[i]["Amount"]}")

    except Exception as e:
        print("Some Error Occured: ", e)
      

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

        get_current_expenses_from_json()

        # Store newly added user data in a dictionary and put it into expense_list
        one_expense={
                "Id" : ide,
                "Title": title,
                "Date" : date_,
                "Amount":amount
        }
        expense_list.append(one_expense)


        with open("expenses_details/full_details.json", "w") as file:
                json.dump(expense_list, file, indent=4)

        print("=================================ADDED SUCCESSFULLY=============================")
    except ValueError as e:
        print("Your typed output is not correct. Please try again: ",e)

def view_expenses_list():
    print("===============================TOTAL EXPENSES===================================\n")
    print_expense_list()

    print("\n================================================================================")

def get_total_spent_amount():
    print("=========================TOTAL AMOUNT SPEND SO FAR==============================")
    total_amount = 0.0
    with open("expenses_details/full_details.json", "r") as file:
        data = json.load(file)
        for j in range(0,len(data)):
            total_amount += data[j]['Amount']


    print(f"Total Amount you spend so far is: {total_amount}")

    print("================================================================================")

def delete_expense_from_list():
    try:
        print("===============================DELETE EXPENSES===================================\n")
        
        # show list for user to see id and other details
        print_expense_list()

        deleted_item_id = str(input("Please enter id of item that you want to delete: "))
        expense_list = []
        is_entered_id_exist = False
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                if(str(items[i]['Id']) != deleted_item_id):
                    expense_list.append(items[i])
                else:
                    is_entered_id_exist = True

        with open("expenses_details/full_details.json", "w") as file:
                    json.dump(expense_list, file, indent=4)
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
        expense_list = []
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                if(str(items[i]['Id']) == 'not_a_id'):
                    expense_list.append(items[i])

        with open("expenses_details/full_details.json", "w") as file:
                    json.dump(expense_list, file, indent=4)
        print("=================================DELETED ALL EXPENSES SUCCESSFULLY=============================\n")
    else:
         print("You didn't confirm from your side to delete all expenses. Please try again\n")
