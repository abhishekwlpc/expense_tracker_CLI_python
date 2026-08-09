import json

try:
# Welcome message
    print("Welcome to the Python Express Tracker!")

    # Operation decision

    operation = input("Enter following number to proceed\nTo Add expense, type 1 and press enter\nTo See all expenses and total amount you send, type 2 and press enter\nTo quit please enter q\n")

    # Add expense logic
    if(operation == "1"):
        print("===============================ADD EXPENSES===================================")
        # Get inputs from the CLI
        title = input("Please enter the expense name/title: ")
        date = input("Please enter the date: ")
        amount = float(input("Please enter the expense amount: "))

        # Store in a list

        expense_list = []
        
        
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                expense_list.append(items[i])
                i+=1

            
        one_expense={
                "Id" : id,
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
                j +=1


        print(f"Total Amount you spend so far is: {total_amount}")

        print("================================================================================")
    elif(operation == "4"):

        print("===============================DELETE EXPENSES===================================")

        expense_list = []
        with open("expenses_details/full_details.json", "r") as file1:
            items = json.load(file1)
            for i in range(0,len(items)):
                expense_list.append(items[i])
                i+=1

        deleted_item = int(input("Please enter id of item that you want to delete: "))
        expense_list.pop(deleted_item-1)

        with open("expenses_details/full_details.json", "w") as file:
                    json.dump(expense_list, file, indent=4)
        print("=================================DELETED SUCCESSFULLY=============================")
except Exception as e:
     print("Some Error Occured", e)                    

# print(f"Total Amount you spend so far is:  {total_amount}")
# print(j)


