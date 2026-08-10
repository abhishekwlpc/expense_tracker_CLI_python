import json
import uuid

# Welcome message
print("Welcome to the Python Express Tracker!")
while True:
    try:
        # Operation decision
        operation = input("** Enter following number to proceed\n-> To Add expense, type 1 and press enter\n-> To See all expenses and total amount you send, type 2 and press enter\n-> To See total spend amount, type 3 and press enter\n-> To Delete an expense from the list, type 4 and press enter\n-> To quit please enter q\n")

        # Add expense logic
        if(operation == "1"):
            print("===============================ADD EXPENSES===================================")
            # Get inputs from the CLI
            title = input("Please enter the expense name/title: ")
            date = input("Please enter the date: ")
            amount = float(input("Please enter the expense amount: "))
            ide = ide = str(uuid.uuid4())

            # Store in a list
            expense_list = []
            
            
            with open("expenses_details/full_details.json", "r") as file1:
                items = json.load(file1)
                for i in range(0,len(items)):
                    expense_list.append(items[i])

                
            one_expense={
                    "Id" : ide,
                    "Title": title,
                    "Date" : date,
                    "Amount":amount
            }

            expense_list.append(one_expense)


            with open("expenses_details/full_details.json", "w") as file:
                    json.dump(expense_list, file, indent=4)

            print("=================================ADDED SUCCESSFULLY=============================")

        elif(operation == "2"):
            print("===============================TOTAL EXPENSES===================================\n")
            with open("expenses_details/full_details.json", "r") as f:
                print(f.read())
            print("================================================================================")

            # Logic to get total amount
        elif(operation == "3"):
            print("=========================TOTAL AMOUNT SPEND SO FAR==============================")
            length = 0
            total_amount = 0.0
            with open("expenses_details/full_details.json", "r") as file:
                data = json.load(file)
                for j in range(0,len(data)):
                    total_amount += data[j]['Amount']


            print(f"Total Amount you spend so far is: {total_amount}")

            print("================================================================================")
        elif(operation == "4"):

            print("===============================DELETE EXPENSES===================================\n")

            # show list for user
            with open("expenses_details/full_details.json", "r") as f:
                print(f.read())
            deleted_item_id = str(input("Please enter id of item that you want to delete: "))

            

            expense_list = []
            with open("expenses_details/full_details.json", "r") as file1:
                items = json.load(file1)
                for i in range(0,len(items)):
                    if(str(items[i]['Id']) != deleted_item_id):
                        expense_list.append(items[i])
                    i+=1

            with open("expenses_details/full_details.json", "w") as file:
                        json.dump(expense_list, file, indent=4)
            print("=================================DELETED SUCCESSFULLY=============================")

        elif(operation =='q' or operation =='quit'):
            break
    except ValueError as e:
         print("Please type 1 or 2 or 3 or 4 or q", e)

    except Exception as e:
        print("Some Error Occured: ", e)